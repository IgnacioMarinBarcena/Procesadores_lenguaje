import ply.lex as lex

class MyLexer():
    # CONSTRUCTOR
    def __init__(self):
        print('Lexer constructor called.')
        self.lexer = lex.lex(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Lexer destructor called.')

    literals = ['+', '-', '*', '/', '(', ')','<','>',';',',','.','&','|','!','[',']','{','}',':']

    # Palabras reservadas
    reserved = {
        # TRUE, FALSE
        'cierto' : 'CIERTO',
        'falso' : 'FALSO',
        # Tipos de variable
        'entero' : 'ENTERO',
        'real' : 'REAL',
        'booleano' : 'BOOLEANO',
        # Operadores lógicos
        'and' : 'AND',
        'or' : 'OR',
        'not' : 'NOT',
        # Condicionales
        'si' : 'SI',
        'sino' : 'SINO',
        'entonces' : 'ENTONCES',
        'finsi' : 'FINSI',
        # Bucles
        'mientras' : 'MIENTRAS',
        'finmientras' : 'FINMIENTRAS',
        # Struct
        'vector' : 'VECTOR',
        'long' : 'LONG',
        'registro' : 'REGISTRO',
        'caracter' : 'CARACTER',
        # Funciones
        'funcion' : 'FUNCION',
        'devolver' : 'DEVOLVER'
    }

    #variables dentro de la clase
    tokens = [
        'NAME', 'NUMBER','SALTO_LINEA','EXPONENCIAL','LOGARITMICA','SENO','COSENO', 'IgualIgual','MayorIgual','MenorIgual','Igualdad','CHAR'
    ] + list(reserved.values())

    # todos los metodos deben tener como primer argumento “self”
    # Tokens --> Expresiones regulares
    t_ignore = " \t"
    t_ignore_comment = "\%.*"

    def t_NUMBER(self, t):
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
    
    def t_CHAR(self, t):
        r"'(.)'"
        return t
    
    # Expresiones operadores lógicos
    def t_IgualIgual(self, t):
        r'=='
        return t
    
    def t_MayorIgual(self, t):
        r'>='
        return t
    
    def t_MenorIgual(self, t):
        r'<='
        return t
    
    def t_Igualdad(self, t):
        r'='
        return t

    def t_SALTO_LINEA(self, t):
        r'\n'
        return t
    
    # Expresiones numéricas
    def t_EXPONENCIAL(self, t):
        r'exp'
        return t

    def t_LOGARITMICA(self, t):
        r'log'
        return t

    def t_SENO(self, t):
        r'sin'
        return t

    def t_COSENO(self, t):
        r'cos'
        return t
    
    # Expresiones para aceptar en minisculas y mayusculas
    # Operadores lógicos
    def t_NOT(self, t):
        r'(?i)not|!'
        t.value = 'not'
        return t
    
    def t_AND(self, t):
        r'(?i)and|&'
        t.value = 'and'
        return t

    def t_OR(self, t):
        r'(?i)or|"|"'
        t.value = 'or'
        return t
    
    def t_NAME(self, t):
        r'((?i)[a-z][a-z0-9_]*)'
        if t.value.lower() in self.reserved:
            t.value = t.value.lower()
        t.type = self.reserved.get(t.value, 'NAME')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def visualizar_tokens(self, fname):    
        try:
            with open(fname,'r') as f:
                s = f.read()
        except IOError:
            print ("Archivo no encontrado:", fname)
        
        lex.input(s)

        with open('lexer.out','w') as file:
            file.write("ANALIZADOR LEXICO\n")
            file.write("-----------------\n\n")
            file.write("--------------------------------\n")
            file.write("----- Programa de ejemplo ------\n")
            file.write("--------------------------------\n")
            file.write("\n\n" + s + "\n\n")
            file.write("\t\t\t\t TOKENS DE ENTRADA\n")
            file.write("\t\t\t\t-------------------\n\n")

            i = 0
            
            while True:
                i += 1
                tokens = lex.token()
                if not tokens:
                    break
                elif len(str(tokens.type)) > 9:
                    file.write(str(i) + "\t Tipo: " + str(tokens.type) + '\t\t Valor: ' + str(tokens.value) + "\n")
                elif len(str(tokens.type)) < 3:
                    file.write(str(i) + "\t Tipo: " + str(tokens.type) + " "*4 + '\t\t\t Valor: ' + str(tokens.value) + "\n")
                elif len(str(tokens.type)) < 6 and len(str(tokens.type)) > 2:
                    file.write(str(i) + "\t Tipo: " + str(tokens.type) + " "*3 + '\t\t\t Valor: ' + str(tokens.value) + "\n")
                else:
                    file.write(str(i) + "\t Tipo: " + str(tokens.type) + " "*3 + '\t\t Valor: ' + str(tokens.value) + "\n")
