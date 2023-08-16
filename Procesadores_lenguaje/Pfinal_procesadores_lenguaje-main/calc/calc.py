# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------
import sys
from myLexer import MyLexer
from myParser import MyParser
sys.path.insert(0, "../..")

# create objects MY LEXER and MY PARSER
myLex = MyLexer()
lexer=myLex.lexer

myPar = MyParser()
parse = myPar.parser

if sys.version_info[0] >= 3:
    raw_input = input

fname="input8.txt"

try:
    f = open(fname, 'r')
except IOError:
    print ("Archivo no encontrado:", fname)

while 1:
    try:
        s = f.read()
    except EOFError:
        break
    if not s:
        break
    myPar.parse(s)
    myLex.visualizar_tokens(fname)