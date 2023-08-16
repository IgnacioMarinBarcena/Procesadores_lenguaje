import math

global mem_value

tokens = (
    'NAME', 'NUMBER', 'OCTAL', 'HEXADECIMAL', 'BINARIO', 'REAL', 'EXP', 'LOG', 'SIN', 'COS', 'INF', 'UNK', 'MEM', 'NL'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_OCTAL(t):
    r'0[0-7]+'
    t.value = int(t.value, 8)
    return t

def t_HEXADECIMAL(t):
    r'0[xX][0-9a-fA-F]+'
    t.value = int(t.value, 16)
    return t

def t_BINARIO(t):
    r'0[bB][01]+'
    t.value = int(t.value[2:], 2)
    return t

def t_REAL(t):
    r'\d+(\.\d+)*([eE][+-]\d+)*'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_EXP(t):
    r"exp"
    return t

def t_LOG(t):
    r"log"
    return t

def t_SIN(t):
    r"sin"
    return t

def t_COS(t):
    r"cos"
    return t

def t_INF(t):
    r"INF"
    t.value = float(t.value)
    return t

def t_UNK(t):
    r"UNK"
    return t

def t_MEM(t):
    r"MEM"
    return t

t_ignore = " \t"

def t_NL(t):
    r'\n|\r|\r\n'
    return t

def t_comment(t):
    r'\%.*'
    pass

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

# dictionary of names
names = {'MEM':0}

def p_statement_line(p):
    '''statement : statement NL statement
                 | NL statement
                 | NL'''

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression '
    print(p[1])

def p_expression_number(p):
    '''termino : NUMBER
                  | OCTAL
                  | HEXADECIMAL
                  | BINARIO
                  | REAL
                  | INF
                  | UNK
                  | MEM
                  '''
    p[0] = p[1]

def p_term_sign(p):
    '''termino : '+' termino
               | '-' termino'''
    if p[1] == '+':
        p[0] = +p[2]
    elif p[1] == '-':
        p[0] = -p[2]

def p_expression_name(p):
    "termino : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_expression_group(p):
    "termino : '(' expression ')'"
    p[0] = p[2]

def p_expression_binop(p):
    '''expression : expression '+' factor
                  | expression '-' factor
                  '''
    if p[2] == '+':
        if p[1] == -float('INF') or p[3] == 'INF':
            p[0] = 'UNK'
        elif p[1] == 'INF' or p[3] == 'INF':
            p[0] = 'INF'
        else:
            p[0] = p[1] + p[3]
    elif p[2] == '-':
        if p[1] == float('INF') and p[3] == float('INF'):
            p[0] = 'UNK'
        elif p[1] == 'INF':
            p[0] = 'INF'
        elif p[3] == 'INF':
            p[0] = -'INF'
        else:
            p[0] = p[1] - p[3]

def p_expression(p):
    '''expression : factor'''
    p[0] = p[1]

def p_factor_termino(p):
    '''factor : factor '*' termino
              | factor '/' termino
              '''
    if p[2] == '*':
        if p[1] == 'UNK' or p[3] == 'UNK':
            p[0] = 'UNK'
        elif (p[1] == float('INF') or p[1] == 0) and (p[3] == float('INF') or p[3] == 0):
            p[0] = 'UNK'
        elif p[1] == 'INF' or p[3] == 'INF':
            p[0] = 'INF'
        else:
            p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[1] == 'UNK' or p[3] == 'UNK':
            p[0] = 'UNK'
        elif p[1] == 0 and p[3] == 0:
            p[0] = 'UNK'
        elif p[1] == float('INF') and p[3] == float('INF'):
            p[0] = 'UNK'
        elif p[1] == 'INF':
            p[0] = 'INF'
        elif p[3] == 'INF':
            p[0] = 0
        elif p[3] == 0:
            p[0] = 'INF'
        else:
            p[0] = p[1] / p[3]

def p_factor(p):
    '''factor : termino'''
    p[0] = p[1]

def p_expression_fun(p):
    '''expression : EXP '(' expression ')'
                  | LOG '(' expression ')'
                  | SIN '(' expression ')'
                  | COS '(' expression ')' '''
    if p[1] == 'exp':
        p[0] = math.exp(p[3])
    elif p[1] == 'log':
        p[0] = math.log10(p[3])
    elif p[1] == 'sin':
        print(p[3])
        p[0] = math.sin(p[3])
    elif p[1] == 'cos':
        print(p[3])
        p[0] = math.cos(p[3])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    elif p == None:
        pass
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

import sys
fname="input.txt"


try:
    with open(fname, 'r') as file:
        f = file.read()
        yacc.parse(f)
except IOError:
    print ("Archivo no encontrado:", fname)
