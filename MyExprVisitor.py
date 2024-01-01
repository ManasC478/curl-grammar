import pprint
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from StudentAPI import StudentAPI
from utils import method_has_path
 
class MyExprVisitor(ExprVisitor):
    def __init__(self):
        super(MyExprVisitor, self).__init__()
        self.paths = set(['schema', 'student']) # set of paths
        self.request_data = {'method': None, 'content_type': None, 'data': None, 'path_base': None,  'path_student_id': None}
 
    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visit(ctx.curl_statement())  # Just visit the self expression
    
    # visit parse tree for curl statement
    def visitCurl_statement(self, ctx: ExprParser.Curl_statementContext):
        
        # GET AND DELETE METHODS
        if ctx.GET_METHOD() or ctx.DELETE_METHOD():
            self.request_data['method'] = str(ctx.GET_METHOD()) if ctx.GET_METHOD() else str(ctx.DELETE_METHOD())
        # POST AND PATCH METHODS
        elif ctx.POST_METHOD() or ctx.PATCH_METHOD():
            self.request_data['method'] = str(ctx.POST_METHOD()) if ctx.POST_METHOD() else str(ctx.PATCH_METHOD())
            
            # CHECK IF HEADER IS VALID
            if not ctx.header:
                raise Exception('Header not found')
            self.visit(ctx.header)
            
            # CHECK IF DATA IS VALID
            if not ctx.data:
                raise Exception('Data payload not found')
            self.visit(ctx.data)
        else:
            raise Exception('Method not found')
        
        
        # CHECK IF URL IS VALID
        if not ctx.requrl:
            raise Exception('Url not found')
        self.visit(ctx.requrl)
        if not method_has_path(self.request_data):
                raise Exception(f'Method "{self.request_data["method"]}" does not have the provided path')
            
        self.execute()
        
    # visit parse tree for url
    def visitUrl(self, ctx: ExprParser.UrlContext):
        student_path = str(ctx.PATH_STUDENT()) if ctx.PATH_STUDENT() else None
        schema_path = str(ctx.PATH_SCHEMA()) if ctx.PATH_SCHEMA() else None
        identifier = str(ctx.UUIDV4()) if ctx.UUIDV4() else None
        
        if (not student_path and not schema_path) or (schema_path and identifier):
            raise Exception('Not valid path')
        
        self.request_data['path_base'] = student_path if student_path else schema_path
        self.request_data['path_student_id'] = identifier
    
    # visit parse tree for content type
    def visitContent_type_header(self, ctx: ExprParser.Content_type_headerContext):
        if not ctx.CONTENT_TYPE():
            raise Exception('Content type not accepted')
        self.request_data['content_type'] = str(ctx.CONTENT_TYPE())
        
    # visit parse tree for data
    def visitJson_payload(self, ctx: ExprParser.Json_payloadContext):
        if not ctx.data:
            raise Exception('No data provided')
        
        self.visit(ctx.data)
        
    def visitJson_obj(self, ctx: ExprParser.Json_objContext):
        data = {}
        i = 0
        while ctx.pair(i):
            key_value = self.visit(ctx.pair(i))
            data[key_value[0]] = key_value[1]
            i += 1
            
        self.request_data['data'] = data
        
    def visitPair(self, ctx: ExprParser.PairContext):
        return (str(ctx.STRING())[1:-1], self.visit(ctx.value()))
        
    
    def visitValue(self, ctx: ExprParser.ValueContext):
        if ctx.STRING():
            if str(ctx.STRING())[1: -1] == "None":
                return None
            return str(ctx.STRING())[1: -1]
        elif ctx.NUMBER():
            return  int(str(ctx.NUMBER()))
        if ctx.arr():
            return self.visit(ctx.arr())
        
    def visitArr(self, ctx: ExprParser.ArrContext):
        i = 0
        arr = []
        while ctx.value(i):
            arr.append(str(self.visit(ctx.value(i))))
            i += 1
        return arr
    
    def execute(self):
        student_api = StudentAPI()
        pp = pprint.PrettyPrinter(indent=4)
        
        print('RESULT ---------------------------------------------------------------')
        if self.request_data['method'] == 'GET':
            if self.request_data['path_base'] == 'schema':
                pp.pprint(student_api.get_schema())
            elif self.request_data['path_base'] == 'student' and not self.request_data['path_student_id']:
                pp.pprint(student_api.get_students())
            else:
                pp.pprint(student_api.get_student(self.request_data['path_student_id']))
        elif self.request_data['method'] == 'DELETE':
            if not self.request_data['path_student_id']:
                pp.pprint(student_api.delete_students())
            else:
                pp.pprint(student_api.delete_student(self.request_data['path_student_id']))
        
        elif self.request_data['method'] == 'POST':
            pp.pprint(student_api.post_student(self.request_data['data']))
        elif self.request_data['method'] == 'PATCH':
            pp.pprint(student_api.patch_student(self.request_data['path_student_id'], self.request_data['data']))