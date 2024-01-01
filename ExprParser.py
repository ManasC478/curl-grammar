# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,26,8,1,1,1,3,1,
        29,8,1,1,1,1,1,1,2,1,2,3,2,35,8,2,1,3,1,3,1,3,3,3,40,8,3,1,3,3,3,
        43,8,3,1,3,3,3,46,8,3,1,4,1,4,3,4,50,8,4,1,5,1,5,1,5,1,5,5,5,56,
        8,5,10,5,12,5,59,9,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,6,1,6,1,6,1,6,
        1,7,1,7,1,7,1,7,5,7,75,8,7,10,7,12,7,78,9,7,1,7,1,7,1,7,1,7,3,7,
        84,8,7,1,8,1,8,1,8,1,8,3,8,90,8,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,
        0,2,1,0,16,19,1,0,20,21,96,0,18,1,0,0,0,2,21,1,0,0,0,4,32,1,0,0,
        0,6,36,1,0,0,0,8,47,1,0,0,0,10,64,1,0,0,0,12,66,1,0,0,0,14,83,1,
        0,0,0,16,89,1,0,0,0,18,19,3,2,1,0,19,20,5,0,0,1,20,1,1,0,0,0,21,
        22,5,1,0,0,22,23,5,2,0,0,23,25,7,0,0,0,24,26,3,4,2,0,25,24,1,0,0,
        0,25,26,1,0,0,0,26,28,1,0,0,0,27,29,3,8,4,0,28,27,1,0,0,0,28,29,
        1,0,0,0,29,30,1,0,0,0,30,31,3,6,3,0,31,3,1,0,0,0,32,34,5,3,0,0,33,
        35,5,22,0,0,34,33,1,0,0,0,34,35,1,0,0,0,35,5,1,0,0,0,36,37,5,4,0,
        0,37,39,7,1,0,0,38,40,5,5,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,42,
        1,0,0,0,41,43,5,23,0,0,42,41,1,0,0,0,42,43,1,0,0,0,43,45,1,0,0,0,
        44,46,5,5,0,0,45,44,1,0,0,0,45,46,1,0,0,0,46,7,1,0,0,0,47,49,5,6,
        0,0,48,50,3,10,5,0,49,48,1,0,0,0,49,50,1,0,0,0,50,9,1,0,0,0,51,52,
        5,7,0,0,52,57,3,12,6,0,53,54,5,8,0,0,54,56,3,12,6,0,55,53,1,0,0,
        0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,60,1,0,0,0,59,57,
        1,0,0,0,60,61,5,9,0,0,61,65,1,0,0,0,62,63,5,7,0,0,63,65,5,9,0,0,
        64,51,1,0,0,0,64,62,1,0,0,0,65,11,1,0,0,0,66,67,5,14,0,0,67,68,5,
        10,0,0,68,69,3,16,8,0,69,13,1,0,0,0,70,71,5,11,0,0,71,76,3,16,8,
        0,72,73,5,8,0,0,73,75,3,16,8,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,
        1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,12,0,0,
        80,84,1,0,0,0,81,82,5,11,0,0,82,84,5,12,0,0,83,70,1,0,0,0,83,81,
        1,0,0,0,84,15,1,0,0,0,85,90,5,14,0,0,86,90,5,15,0,0,87,90,3,14,7,
        0,88,90,5,13,0,0,89,85,1,0,0,0,89,86,1,0,0,0,89,87,1,0,0,0,89,88,
        1,0,0,0,90,17,1,0,0,0,12,25,28,34,39,42,45,49,57,64,76,83,89
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'curl'", "'-X'", "'-H Content-Type:'", 
                     "'http://studentdb.com/'", "'/'", "'-d'", "'{'", "','", 
                     "'}'", "':'", "'['", "']'", "'None'", "<INVALID>", 
                     "<INVALID>", "'GET'", "'POST'", "'PATCH'", "'DELETE'", 
                     "'student'", "'schema'", "'application/json'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STRING", "NUMBER", "GET_METHOD", 
                      "POST_METHOD", "PATCH_METHOD", "DELETE_METHOD", "PATH_STUDENT", 
                      "PATH_SCHEMA", "CONTENT_TYPE", "UUIDV4", "HEX_4", 
                      "HEX", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_curl_statement = 1
    RULE_content_type_header = 2
    RULE_url = 3
    RULE_json_payload = 4
    RULE_json_obj = 5
    RULE_pair = 6
    RULE_arr = 7
    RULE_value = 8

    ruleNames =  [ "prog", "curl_statement", "content_type_header", "url", 
                   "json_payload", "json_obj", "pair", "arr", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    STRING=14
    NUMBER=15
    GET_METHOD=16
    POST_METHOD=17
    PATCH_METHOD=18
    DELETE_METHOD=19
    PATH_STUDENT=20
    PATH_SCHEMA=21
    CONTENT_TYPE=22
    UUIDV4=23
    HEX_4=24
    HEX=25
    NEWLINE=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def curl_statement(self):
            return self.getTypedRuleContext(ExprParser.Curl_statementContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.curl_statement()
            self.state = 19
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Curl_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.method = None # Token
            self.header = None # Content_type_headerContext
            self.data = None # Json_payloadContext
            self.requrl = None # UrlContext

        def url(self):
            return self.getTypedRuleContext(ExprParser.UrlContext,0)


        def GET_METHOD(self):
            return self.getToken(ExprParser.GET_METHOD, 0)

        def POST_METHOD(self):
            return self.getToken(ExprParser.POST_METHOD, 0)

        def PATCH_METHOD(self):
            return self.getToken(ExprParser.PATCH_METHOD, 0)

        def DELETE_METHOD(self):
            return self.getToken(ExprParser.DELETE_METHOD, 0)

        def content_type_header(self):
            return self.getTypedRuleContext(ExprParser.Content_type_headerContext,0)


        def json_payload(self):
            return self.getTypedRuleContext(ExprParser.Json_payloadContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_curl_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCurl_statement" ):
                listener.enterCurl_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCurl_statement" ):
                listener.exitCurl_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCurl_statement" ):
                return visitor.visitCurl_statement(self)
            else:
                return visitor.visitChildren(self)




    def curl_statement(self):

        localctx = ExprParser.Curl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_curl_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(ExprParser.T__0)
            self.state = 22
            self.match(ExprParser.T__1)
            self.state = 23
            localctx.method = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                localctx.method = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 24
                localctx.header = self.content_type_header()


            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 27
                localctx.data = self.json_payload()


            self.state = 30
            localctx.requrl = self.url()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Content_type_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTENT_TYPE(self):
            return self.getToken(ExprParser.CONTENT_TYPE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_content_type_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContent_type_header" ):
                listener.enterContent_type_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContent_type_header" ):
                listener.exitContent_type_header(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContent_type_header" ):
                return visitor.visitContent_type_header(self)
            else:
                return visitor.visitChildren(self)




    def content_type_header(self):

        localctx = ExprParser.Content_type_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_content_type_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ExprParser.T__2)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 33
                self.match(ExprParser.CONTENT_TYPE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UrlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATH_STUDENT(self):
            return self.getToken(ExprParser.PATH_STUDENT, 0)

        def PATH_SCHEMA(self):
            return self.getToken(ExprParser.PATH_SCHEMA, 0)

        def UUIDV4(self):
            return self.getToken(ExprParser.UUIDV4, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl" ):
                listener.enterUrl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl" ):
                listener.exitUrl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUrl" ):
                return visitor.visitUrl(self)
            else:
                return visitor.visitChildren(self)




    def url(self):

        localctx = ExprParser.UrlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(ExprParser.T__3)
            self.state = 37
            _la = self._input.LA(1)
            if not(_la==20 or _la==21):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(ExprParser.T__4)


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 41
                self.match(ExprParser.UUIDV4)


            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 44
                self.match(ExprParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_payloadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.data = None # Json_objContext

        def json_obj(self):
            return self.getTypedRuleContext(ExprParser.Json_objContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_json_payload

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_payload" ):
                listener.enterJson_payload(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_payload" ):
                listener.exitJson_payload(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson_payload" ):
                return visitor.visitJson_payload(self)
            else:
                return visitor.visitChildren(self)




    def json_payload(self):

        localctx = ExprParser.Json_payloadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_json_payload)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(ExprParser.T__5)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 48
                localctx.data = self.json_obj()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Json_objContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.PairContext)
            else:
                return self.getTypedRuleContext(ExprParser.PairContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_json_obj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson_obj" ):
                listener.enterJson_obj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson_obj" ):
                listener.exitJson_obj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson_obj" ):
                return visitor.visitJson_obj(self)
            else:
                return visitor.visitChildren(self)




    def json_obj(self):

        localctx = ExprParser.Json_objContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_json_obj)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.match(ExprParser.T__6)
                self.state = 52
                self.pair()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 53
                    self.match(ExprParser.T__7)
                    self.state = 54
                    self.pair()
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 60
                self.match(ExprParser.T__8)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(ExprParser.T__6)
                self.state = 63
                self.match(ExprParser.T__8)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def value(self):
            return self.getTypedRuleContext(ExprParser.ValueContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_pair

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair" ):
                listener.enterPair(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair" ):
                listener.exitPair(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair" ):
                return visitor.visitPair(self)
            else:
                return visitor.visitChildren(self)




    def pair(self):

        localctx = ExprParser.PairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pair)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ExprParser.STRING)
            self.state = 67
            self.match(ExprParser.T__9)
            self.state = 68
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ValueContext)
            else:
                return self.getTypedRuleContext(ExprParser.ValueContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_arr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArr" ):
                listener.enterArr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArr" ):
                listener.exitArr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr" ):
                return visitor.visitArr(self)
            else:
                return visitor.visitChildren(self)




    def arr(self):

        localctx = ExprParser.ArrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arr)
        self._la = 0 # Token type
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(ExprParser.T__10)
                self.state = 71
                self.value()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 72
                    self.match(ExprParser.T__7)
                    self.state = 73
                    self.value()
                    self.state = 78
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 79
                self.match(ExprParser.T__11)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(ExprParser.T__10)
                self.state = 82
                self.match(ExprParser.T__11)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def arr(self):
            return self.getTypedRuleContext(ExprParser.ArrContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = ExprParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ExprParser.STRING)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(ExprParser.NUMBER)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.arr()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.match(ExprParser.T__12)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





