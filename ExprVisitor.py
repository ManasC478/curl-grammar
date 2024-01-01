# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#curl_statement.
    def visitCurl_statement(self, ctx:ExprParser.Curl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#content_type_header.
    def visitContent_type_header(self, ctx:ExprParser.Content_type_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#url.
    def visitUrl(self, ctx:ExprParser.UrlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#json_payload.
    def visitJson_payload(self, ctx:ExprParser.Json_payloadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#json_obj.
    def visitJson_obj(self, ctx:ExprParser.Json_objContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pair.
    def visitPair(self, ctx:ExprParser.PairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arr.
    def visitArr(self, ctx:ExprParser.ArrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#value.
    def visitValue(self, ctx:ExprParser.ValueContext):
        return self.visitChildren(ctx)



del ExprParser