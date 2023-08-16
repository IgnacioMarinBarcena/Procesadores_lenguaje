# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import math
import sys
sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = (
    'NAME', 'NUMBER','SALTO_LINEA','EXPONENCIAL','LOGARITMICA','SENO','COSENO','INFINITO','UNKNOWN','MEMORIA'
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens
t_NAME = r'[a-zA-Z0-9_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'0[0-7]+|0[xX][\da-fA-F]+|0[bB][01]+|\d+(\.\d+)?([eE][+-]?\d+)?'
    if '.' in t.value or 'E' in t.value or 'e' in t.value:
        t.value = float(t.value)
    elif t.value.startswith(('0B','0b')):
        t.value = int(t.value,2)
    elif t.value.startswith(('0X','0x')):
        t.value = int(t.value,16)
    elif t.value.startswith('0'):
        t.value = int(t.value,8)
    else:
        t.value = int(t.value,0)
    return t

t_ignore = " \t"
t_ignore_comment = "\%.*"

def t_SALTO_LINEA(t):
    r'\n'
    return t

def t_EXPONENCIAL(t):
    r'exp'
    return t

def t_LOGARITMICA(t):
    r'log'
    return t

def t_SENO(t):
    r'sin'
    return t

def t_COSENO(t):
    r'cos'
    return t

def t_INFINITO(t):
    r'inf'
    return t

def t_UNKNOWN(t):
    r'UNK'
    return t

def t_MEMORIA(t):
    r'MEM'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# dictionary of names
names = {'MEM':0}

# Declaramos los statements
def p_statements(p):
    '''statements : statement SALTO_LINEA statements
                  | statement'''

def p_statement_salto_linea(p):
    'statement : \n'

def p_statement_assign(p):
    '''statement : MEMORIA '=' expression '''
    names[p[1]] = p[3]
    print(f'{p[1]} = {names[p[1]]}') # Mostramos el valor que tiene MEM

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

# Expressiones
def p_expression_multiplicador(p):
    'expression : multiplicador'
    p[0] = p[1]

def p_multiplicador(p):
    'multiplicador : operando'
    p[0] = p[1]

def p_expression_operando_number(p):
    '''operando : NUMBER
                | INFINITO 
                | UNKNOWN '''
    if p[1] == 'inf':
        p[0] = float(p[1])
    else:
        p[0] = p[1]

def p_expression_group(p):
    "operando : '(' expression ')'"
    p[0] = p[2]

def p_expression_operando_signo(p):
    '''operando : '+' operando
                | '-' operando'''
    if p[1] == '+':
        p[0] = +p[2]
    elif p[1] == '-':
        p[0] = -p[2]

def p_expression_binop(p):
    '''expression : expression '+' multiplicador
                  | expression '-' multiplicador '''
    if p[2] == '+':
        if p[1] == 'inf' or p[3] == 'inf':
            p[0] = 'inf'
        elif p[1] == 'inf' and p[3] == 'INF':
            p[0] = 'inf'
        elif p[1] == -float('inf') and p[3] == float('inf'):
            p[0] = 'UNK'
        else: 
            p[0] = p[1] + p[3]
    elif p[2] == '-':
        if p[1] == 'inf':
            p[0] = 'inf'
        elif p[3] == 'inf':
            p[0] = -float('inf')
        elif p[1] == float('inf') and p[3] == float('inf'):
            p[0] = 'UNK'
        elif p[1] == float('inf') and p[3] == -float('inf'):
            p[0] = 'UNK'
        else:
            p[0] = p[1] - p[3]

def p_multiplicador_operando(p):
    '''multiplicador : multiplicador '*' operando
                     | multiplicador '/' operando '''
    if p[2] == '*':
        if p[1] == 'inf' or p[3] == 'inf':
            p[0] = 'inf'
        elif p[1] == 0:
            if p[3] == float('inf') or p[3] == 'UNK':
                p[0] = 'UNK'
        elif p[3] == 0:
            if p[1] == 'inf' or p[1] == 'UNK':
                p[0] = 'UNK'
        elif p[1] == float('inf') and p[3] == 'UNK':
            p[0] = 'UNK'
        elif p[1] == 'UNK' and p[3] == float('inf'):
            p[0] = 'UNK'
        elif p[1] == 'UNK' or p[3] == 'UNK':
            p[0] = 'UNK'
        else:
            p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[1] == float('inf') and p[3] == float('inf'):
            p[0] = 'UNK'
        elif p[1] == 'inf': 
            if p[3] < 0:
                p[0] = -float('inf')
            elif p[3] > 0:
                p[0] = 'inf'
        elif p[1] == -float('inf'):
            if p[3] < 0:
                p[0] = 'inf'
            elif p[3] > 0:
                p[0] == -float('inf')
        elif p[3] == 'inf':
            p[0] = 0
        elif p[3] == 0 and p[1] == 0:
            p[0] = 'UNK'
        elif p[3] == 0:
            p[0] = float('inf')
        else:
            p[0] = p[1] / p[3]

def p_operando_cient(p):
    '''operando : EXPONENCIAL '(' expression ')'
                  | LOGARITMICA '(' expression ')'
                  | SENO '(' expression ')'
                  | COSENO '(' expression ')' '''

    if p[1] == 'exp':
        p[0] = math.exp(float(p[3]))
    elif p[1] == 'log':
        p[0] = math.log10(float(p[3]))
    elif p[1] == 'sin':
        p[0] = math.sin(float(p[3]))
    elif p[1] == 'cos':
        p[0] = math.cos(float(p[3]))

def p_operando_name(p):
    "operando : MEMORIA"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print(p)
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

fname="input.txt"

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
    yacc.parse(s)


