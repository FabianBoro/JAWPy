import px_lexer
import px_parser
import px_interpreter

from sys import *

#IMEDIATELLY / LANGSUNG
if __name__ == '__main__':
    lexer = px_lexer.BasicLexer()
    parser = px_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('px > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            px_interpreter.BasicExecute(tree, env)
