import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main(argv):
    
    
    user_input = input("Enter a curl statement: ")
    input_stream = InputStream(user_input)
    
    while input_stream:
        #input = StdinStream()
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)
        tree = parser.prog()
        try: 
            MyExprVisitor().visitProg(tree) # Evaluate the expression
        except Exception as e:
            print('Syntax Error: ', e)
            
        again = input("Do you want to make another request? (Y/y): ")
        if again == "Y" or again == "y":
            user_input = input("Enter a curl statement: ")
            input_stream = InputStream(user_input)
        else:
            input_stream = None

if __name__ == '__main__':
    main(sys.argv)