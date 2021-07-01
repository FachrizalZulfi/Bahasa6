import bahasa6_lexer
import bahasa6_parser
import bahasa6_interp

from sys import *

#DENGAN MASUKAN EKSTENSI .six
lexer = bahasa6_lexer.BasicLexer()
parser = bahasa6_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    bahasa6_interp.BasicExecute(tree, env)
