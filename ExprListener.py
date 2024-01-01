# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#curl_statement.
    def enterCurl_statement(self, ctx:ExprParser.Curl_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#curl_statement.
    def exitCurl_statement(self, ctx:ExprParser.Curl_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#content_type_header.
    def enterContent_type_header(self, ctx:ExprParser.Content_type_headerContext):
        pass

    # Exit a parse tree produced by ExprParser#content_type_header.
    def exitContent_type_header(self, ctx:ExprParser.Content_type_headerContext):
        pass


    # Enter a parse tree produced by ExprParser#url.
    def enterUrl(self, ctx:ExprParser.UrlContext):
        pass

    # Exit a parse tree produced by ExprParser#url.
    def exitUrl(self, ctx:ExprParser.UrlContext):
        pass


    # Enter a parse tree produced by ExprParser#json_payload.
    def enterJson_payload(self, ctx:ExprParser.Json_payloadContext):
        pass

    # Exit a parse tree produced by ExprParser#json_payload.
    def exitJson_payload(self, ctx:ExprParser.Json_payloadContext):
        pass


    # Enter a parse tree produced by ExprParser#json_obj.
    def enterJson_obj(self, ctx:ExprParser.Json_objContext):
        pass

    # Exit a parse tree produced by ExprParser#json_obj.
    def exitJson_obj(self, ctx:ExprParser.Json_objContext):
        pass


    # Enter a parse tree produced by ExprParser#pair.
    def enterPair(self, ctx:ExprParser.PairContext):
        pass

    # Exit a parse tree produced by ExprParser#pair.
    def exitPair(self, ctx:ExprParser.PairContext):
        pass


    # Enter a parse tree produced by ExprParser#arr.
    def enterArr(self, ctx:ExprParser.ArrContext):
        pass

    # Exit a parse tree produced by ExprParser#arr.
    def exitArr(self, ctx:ExprParser.ArrContext):
        pass


    # Enter a parse tree produced by ExprParser#value.
    def enterValue(self, ctx:ExprParser.ValueContext):
        pass

    # Exit a parse tree produced by ExprParser#value.
    def exitValue(self, ctx:ExprParser.ValueContext):
        pass



del ExprParser