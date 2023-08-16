import math
import ply.yacc as yacc
from myLexer import MyLexer

mylex = MyLexer()

class MyParser():
    # Constructor
    # CONSTRUCTOR
    def __init__(self):
        print('Parser constructor called.')
        self.parser = yacc.yacc(module=self)

    # DESTRUCTOR
    def __del__(self):
        print('Parser destructor called.')

    # variables dentro de la clase
    # dictionary of nombres de variables (valores)
    names = {}
    tipo = ""
    valor = ""

    # dictionary de registros
    registros = {}
    variables_registros = {}
    temporal = {}

    # dictionary de vectores
    vectors = {}
    lista_vectores = []

    # dictionary de funciones
    funciones = {}
    inputs_temporal = {}

    # tokens
    tokens = mylex.tokens

    # Gramática
    # =================================================
    def p_statements(self, p):
        '''statements : statement SALTO_LINEA statements
                      | statement '''

    def p_statement_salto_linea(self, p):
        '''statement : \n
                     | asignacion
                     | declaracion
                     | vectores
                     | registros 
                     | def_funcion
                     | uso_funcion
                     | condicionales
                     | bucles '''
        print()
        print("STATEMENT")
        print("=========")
        print()
        print(self.registros)
        print()
        print(self.variables_registros)
        print()
        print(self.vectors)
        print()
        print(self.lista_vectores)
        print()
        print(self.names)
        print()
        print(self.funciones)
        print()

    def p_statement_expr(self, p):
        '''statement : logico'''
        p[0] = p[1]
        if type(p[1]) is not dict and p[1] != None:
            print(p[1])
    
    def p_declaracion(self, p):
        '''declaracion : tipo names
                       | VECTOR tipo NAME '[' NUMBER ']' 
                       | REGISTRO NAME '{' atributos '}' '''
    
        if p[1] == 'vector':
            if p[3] in self.vectors:
                print("ERROR: Este vector ya esta declarado")
            else:
                if p[3] in self.names or p[3] in self.registros:
                    print("ERROR: Se intenta declarar a un vector con un nombre de una variable ya declarada")
                else:
                    self.vectors[p[3]] =  {"tipo":p[2], "tamaño":p[5]}
                    i = 0
                    elem_vector = []
                    while i < p[5]:
                        elem_vector.append(0)
                        i += 1
                    self.lista_vectores.append({"nombre_vector": p[3], "valores": elem_vector})
        elif p[1] == 'registro':
            if p[2] in self.registros:
                print("ERROR: Este registro ya esta declarado")
            else:
                if p[2] in self.names or p[2] in self.vectors:
                    print("ERROR: Se intenta declarar a un registro con un nombre de una variable ya declarada")
                else:
                    if len(self.temporal) != 0:
                        self.registros[p[2]] =  self.temporal
                        self.temporal = {}
                    
    # Asignaciones
    def p_asignacion_assign(self, p):
        '''asignacion : tipo NAME Igualdad logico
                     | NAME Igualdad logico '''
        
        if p[2] not in self.names and p[2] != None and (p[1] == "entero" or p[1] == "real" or p[1] == "booleano" or p[1] == "caracter"):
            if (type(p[4]) is int and p[1] == "entero") or (type(p[4]) is bool and p[1] == "booleano") or (type(p[4]) is float and p[1] == "real") or (type(p[4]) is str and p[1] == "caracter"):
                self.names[p[2]] =  {"tipo":p[1], "valor":p[4]}
            elif p[1] != None and p[1] != "entero" and p[1] != "booleano" and p[1] != "real" and p[1] != "caracter":
                print("ERROR: Tipo de variable no valido")
            else:
                print("ERROR: El tipo de la variable no coincide con el tipo del valor que se le quiere asignar") 
        elif p[1] in self.names:
            if (type(p[3]) is int and self.names[p[1]]['tipo'] == "entero") or (type(p[3]) is bool and self.names[p[1]]['tipo'] == "booleano") or (type(p[3]) is float and self.names[p[1]]['tipo'] == "real") or (type(p[3]) is str and self.names[p[1]]['tipo'] == "caracter"):
                self.names[p[1]]['valor'] = p[3]
            elif p[3] != None:
                print("ERROR: El tipo de la variable no coincide con el tipo del valor que se le quiere asignar")
        else:
            print("ERROR: La variable no se encuentra declarada")
                
    # NAMES
    def p_names_name(self, p):
        '''names : NAME ',' names
                 | NAME '''
 
        if p[1] in self.names:
            print()
            print("ERROR: La variable ya se ha declarado")
            print()
        else:
            self.names[p[1]] =  {"tipo":self.tipo, "valor":None}

    # TIPO
    def p_tipo_tipos(self, p):
        '''tipo : BOOLEANO
                | ENTERO
                | REAL 
                | CARACTER 
                | REGISTRO
                | VECTOR 
                | NAME '''
        if p[1] in self.vectors or p[1] in self.registros or p[1] == 'vector' or p[1] == 'registro' or p[1] == 'caracter' or p[1] == 'real' or p[1] == 'entero' or p[1] == 'booleano':
            self.tipo = p[1]
            p[0] = p[1]
        else:
            print("ERROR: No se contempla ese tipo de variable: ",p[1])
    
    # VECTOR
    def p_vectores_vector(self, p):
        '''vectores : NAME '[' NUMBER ']' Igualdad logico '''

        if p[1] not in self.names and p[1] in self.vectors:
            if p[3] > self.vectors[p[1]]['tamaño']:
                print("ERROR: Indice fuera de rango")
            elif (type(p[6]) is int and self.vectors[p[1]]['tipo'] == "entero") or (type(p[6]) is bool and self.vectors[p[1]]['tipo'] == "booleano") or (type(p[6]) is float and self.vectors[p[1]]['tipo'] == "real") or (type(p[6]) is str and self.vectors[p[1]]['tipo'] == "caracter"):
                i = 0
                for elem in self.lista_vectores:
                    if self.lista_vectores[i]['nombre_vector'] == p[1]:
                        self.lista_vectores[i]['valores'][p[3]] = p[6]
                    i += 1
            else:
                print("ERROR: Tipo del valor no coincide con el tipo del vector")
        else:
            print("ERROR: Se intenta acceder a un vector no declarado")
    
    # REGISTROS
    def p_registros_registro(self,p):
        '''registros : NAME '.' NAME Igualdad logico
                     | NAME NAME '''
        
        if p[1] not in self.registros:
            if p[1] not in self.variables_registros:
                print("ERROR: Intento de acceso a una variable no declarada")
            elif p[1] in self.variables_registros:
                x = self.variables_registros[p[1]]['tipo']
                if (self.registros[x][p[3]] == 'entero' and type(p[5]) is int) or (self.registros[x][p[3]] == 'real' and type(p[5]) is float) or (self.registros[x][p[3]] == 'booleano' and type(p[5]) is bool) or (self.registros[x][p[3]] == 'caracter' and type(p[5]) is str):
                    self.variables_registros[p[1]]['valores'][p[3]]= p[5]
                elif self.registros[x][p[3]] == 'vector' or self.registros[x][p[3]] == 'registro' or self.registros[x][p[3]] in self.vectors or self.registros[x][p[3]] in self.registros:
                    self.variables_registros[p[1]]['valores'][p[3]]= p[5]
                else:
                    print("ERROR: El tipo de valor no corresponde con el tipo de la variable")
            else:
                print("ERROR: Intento de acceso a un registro no declarado")
        else:
            self.variables_registros[p[2]] =  {"tipo":p[1], "valores":{}}
            for key in self.registros[p[1]].keys():
                self.variables_registros[p[2]]["valores"][key] = "None"

    def p_atributos(self, p):
        '''atributos : tipo campos ';' atributos
                     | tipo campos ';' '''
        self.tipo = p[1]
    
    def p_campos(self,p):
        '''campos : NAME ',' campos
                  | NAME '''
        
        if self.tipo == 'registro' and p[1] not in self.registros:
            print("ERROR: No se puede asignar a un registro un registro no declarado anteriormente")
            self.temporal = {}
        elif self.tipo == 'vector' and p[1] not in self.vectors:
            print("ERROR: No se puede asignar a un registro un vector no declarado anteriormente")
            self.temporal = {}
        else:
            self.temporal[p[1]] = self.tipo
    
    # Funciones
    def p_deffunc_funcion(self, p):
        '''def_funcion : FUNCION NAME '(' list_args ')' ':' tipo '{' blq_sentencia DEVOLVER blq_sentencia '}' '''
        if p[2] in self.names or p[2] in self.vectors or p[2] in self.variables_registros:
            print("ERROR: No se puede declarar una función con un nombre ya empleado")
        else:
            self.names[p[11]] = {'tipo':p[7],'valor':None}
            self.funciones[p[2]] = {'Argumentos' : self.inputs_temporal, 'salida' : {'tipo' : p[7], 'variable' : p[11]}}
            self.inputs_temporal = {}
            
    def p_usofunc_funcion(self, p):
        '''uso_funcion : NAME '(' argumentos ')' '''
        if p[1] not in self.funciones:
            print("ERROR: Llamada a una funcion que no se encuentra definida")
        else:
            print("PROXIMAMENTE: No se ha implementado el uso de funciones aún")
    
    def p_listargs_sentencia(self, p):
        '''list_args : tipo NAME ',' list_args
                     | tipo NAME
                     | empty '''
        
        if p[1] == " ":
            p[0] = p[1]
        else:
            if p[2] in self.names:
                print()
                print("ERROR: La variable ya se ha declarado")
                print()
            else:
                self.names[p[2]] =  {"tipo":self.tipo, "valor":None}
                self.inputs_temporal[p[2]] = self.tipo
                
    def p_blq_sentencias(self,p):
        '''blq_sentencia : statement SALTO_LINEA blq_sentencia
                         | statement '''
        p[0] = p[1]

    def p_argumentos(self, p):
        '''argumentos : argumentos ',' operando
                      | operando
                      | empty '''
        p[0] = p[1]
    
    # Control de flujo
    def p_condicionales(self, p):
        '''condicionales : SI blq_sentencia ENTONCES blq_sentencia FINSI
                         | SI blq_sentencia ENTONCES blq_sentencia SINO blq_sentencia FINSI '''
    
    def p_bucles(self, p):
        '''bucles : MIENTRAS logico blq_sentencia FINMIENTRAS '''
    
    def p_empty(self, p):
        '''empty : '''
        p[0] = " "

    # Restricciones --> bucles y condicionales
    def p_restriccion(self, p):
        '''restriccion : restriccion comparador expression
                       | expression '''
        if len(p) == 2: 
            p[0] = p[1]
        else:
            if p[2] == '<':
                if type(p[1]) is dict and type(p[3]) is not dict:
                    x = p[1]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x < p[3]:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[3]) is dict and type(p[1]) is not dict:
                    x = p[3]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] < x:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[1]) is dict and type(p[3]) is dict:
                    x = p[1]['valor']
                    y = p[3]['valor']
                    if x == None or y == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x < y:
                        p[0] = True
                    else:
                        p[0] = False
                else:
                    if p[1] == None or p[3] == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] < p[3]:
                        p[0] = True
                    else:
                        p[0] = False
            elif p[2] == '<=':
                if type(p[1]) is dict and type(p[3]) is not dict:
                    x = p[1]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x <= p[3]:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[3]) is dict and type(p[1]) is not dict:
                    x = p[3]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] <= x:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[1]) is dict and type(p[3]) is dict:
                    x = p[1]['valor']
                    y = p[3]['valor']
                    if x == None or y == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x <= y:
                        p[0] = True
                    else:
                        p[0] = False
                else:
                    if p[1] == None or p[3] == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] <= p[3]:
                        p[0] = True
                    else:
                        p[0] = False
            elif p[2] == '>':
                if type(p[1]) is dict and type(p[3]) is not dict:
                    x = p[1]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x > p[3]:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[3]) is dict and type(p[1]) is not dict:
                    x = p[3]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] > x:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[1]) is dict and type(p[3]) is dict:
                    x = p[1]['valor']
                    y = p[3]['valor']
                    if x == None or y == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x > y:
                        p[0] = True
                    else:
                        p[0] = False
                else:
                    if p[1] == None or p[3] == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] > p[3]:
                        p[0] = True
                    else:
                        p[0] = False
            elif p[2] == '>=':
                if type(p[1]) is dict and type(p[3]) is not dict:
                    x = p[1]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x >= p[3]:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[3]) is dict and type(p[1]) is not dict:
                    x = p[3]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] >= x:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[1]) is dict and type(p[3]) is dict:
                    x = p[1]['valor']
                    y = p[3]['valor']
                    if x == None or y == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x >= y:
                        p[0] = True
                    else:
                        p[0] = False
                else:
                    if p[1] == None or p[3] == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] >= p[3]:
                        p[0] = True
                    else:
                        p[0] = False
            elif p[2] == '==':
                if type(p[1]) is dict and type(p[3]) is not dict:
                    x = p[1]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x == p[3]:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[3]) is dict and type(p[1]) is not dict:
                    x = p[3]['valor']
                    if x == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] == x:
                        p[0] = True
                    else:
                        p[0] = False
                elif type(p[1]) is dict and type(p[3]) is dict:
                    x = p[1]['valor']
                    y = p[3]['valor']
                    if x == None or y == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif x == y:
                        p[0] = True
                    else:
                        p[0] = False
                else:
                    if p[1] == None or p[3] == None:
                        print("ERROR: No se puede comparar valores de tipo Nontype")
                    elif p[1] == p[3]:
                        p[0] = True
                    else:
                        p[0] = False

    def p_logico(self, p):
        '''logico : logico condicion restriccion
                  | restriccion '''
        p[0] = p[1]
    
    def p_comparador(self, p):
        '''comparador : IgualIgual
                      | MenorIgual
                      | MayorIgual
                      | Igualdad
                      | '<'
                      | '>'  '''
        p[0] = p[1]      
    
    def p_condicion(self, p):
        '''condicion : OR
                     | AND
                     | NOT 
                     | '!'
                     | '&'
                     | '|' '''
        p[0] = p[1]

    # EXPRESSION
    def p_expression_multiplicador(self, p):
        '''expression : multiplicador '''
        p[0] = p[1]
    
    def p_multiplicador(self, p):
        'multiplicador : operando'
        p[0] = p[1]

    def p_expression_binop(self, p):
        '''expression : expression '+' multiplicador
                    | expression '-' multiplicador'''
        if p[2] == '+':
            if type(p[1]) is dict or type(p[3]) is dict:
                if (type(p[1]) is dict and p[1]['tipo'] == 'booleano') or (type(p[3]) is dict and p[3]['tipo'] == 'booleano'):
                        print("ERROR: No se pueden realizar operaciones aritméticas con booleanos")
                else:
                    if type(p[1]) is dict and type(p[3]) is not dict:
                        if p[1]['valor'] is None:
                            print("ERROR: No se puede sumar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and type(p[3]) is int:
                                p[0] = int(p[1]['valor'] + p[3])
                            elif p[1]['tipo'] == 'caracter' and type(p[3]) is str:
                                p[0] = str(p[1]['valor'] + p[3])
                            elif p[1]['tipo'] == 'real' and type(p[3]) is float:
                                p[0] = float(p[1]['valor'] + p[3])
                    elif type(p[3]) is dict and type(p[1]) is not dict:
                        if p[3]['valor'] is None:
                            print("ERROR: No se puede sumar variables con el valor None")
                        else:
                            if p[3]['tipo'] == 'entero' and type(p[1]) is int:
                                p[0] = int(p[1] + p[3]['valor'])
                            elif p[3]['tipo'] == 'caracter' and type(p[1]) is str:
                                p[0] = str(p[1] + p[3]['valor'])
                            elif p[3]['tipo'] == 'real' and type(p[1]) is float:
                                p[0] = float(p[1] + p[3]['valor'])
                    elif type(p[1]) is dict and type(p[3]) is dict:
                        if p[1]['valor'] is None or p[3]['valor'] is None:
                            print("ERROR: No se puede sumar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and p[3]['tipo'] == 'entero':
                                p[0] = int(p[1]['valor'] + p[3]['valor'])
                            elif p[1]['tipo'] == 'caracter' and p[3]['tipo'] == 'caracter':
                                p[0] = str(p[1]['valor'] + p[3]['valor'])
                            elif p[1]['tipo'] == 'real' and p[3]['tipo'] == 'real':
                                p[0] = float(p[1]['valor'] + p[3]['valor'])
            else:
                if type(p[1]) is int and type(p[3]) is int:
                    p[0] = int(p[1] + p[3])
                elif type(p[1]) is str and type(p[3]) is str:
                    p[0] = str(p[1] + p[3])
                elif type(p[1]) is float and type(p[3]) is float:
                    p[0] = float(p[1] + p[3])
        elif p[2] == '-':
            if type(p[1]) is dict or type(p[3]) is dict:
                if (type(p[1]) is dict and p[1]['tipo'] == 'booleano') or (type(p[3]) is dict and p[3]['tipo'] == 'booleano'):
                        print("ERROR: No se pueden realizar operaciones aritméticas con booleanos")
                else:
                    if type(p[1]) is dict and type(p[3]) is not dict:
                        if p[1]['valor'] is None:
                            print("ERROR: No se puede restar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and type(p[3]) is int:
                                p[0] = int(p[1]['valor'] - p[3])
                            elif p[1]['tipo'] == 'caracter' and type(p[3]) is str:
                                p[0] = str(p[1]['valor'] - p[3])
                            elif p[1]['tipo'] == 'real' and type(p[3]) is float:
                                p[0] = float(p[1]['valor'] - p[3])
                    elif type(p[3]) is dict and type(p[1]) is not dict:
                        if p[3]['valor'] is None:
                            print("ERROR: No se puede restar variables con el valor None")
                        else:
                            if p[3]['tipo'] == 'entero' and type(p[1]) is int:
                                p[0] = int(p[1] - p[3]['valor'])
                            elif p[3]['tipo'] == 'caracter' and type(p[1]) is str:
                                p[0] = str(p[1] - p[3]['valor'])
                            elif p[3]['tipo'] == 'real' and type(p[1]) is float:
                                p[0] = float(p[1] - p[3]['valor'])
                    elif type(p[1]) is dict and type(p[3]) is dict:
                        if p[1]['valor'] is None or p[3]['valor'] is None:
                            print("ERROR: No se puede restar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and p[3]['tipo'] == 'entero':
                                p[0] = int(p[1]['valor'] - p[3]['valor'])
                            elif p[1]['tipo'] == 'caracter' and p[3]['tipo'] == 'caracter':
                                p[0] = str(p[1]['valor'] - p[3]['valor'])
                            elif p[1]['tipo'] == 'real' and p[3]['tipo'] == 'real':
                                p[0] = float(p[1]['valor'] - p[3]['valor'])
            else:
                if type(p[1]) is int and type(p[3]) is int:
                    p[0] = int(p[1] - p[3])
                elif type(p[1]) is str and type(p[3]) is str:
                    p[0] = str(p[1] - p[3])
                elif type(p[1]) is float and type(p[3]) is float:
                    p[0] = float(p[1] - p[3])
    
    def p_expression_operando_number(self, p):
        '''operando : NUMBER
                    | CHAR
                    | CIERTO
                    | FALSO '''
        if p[1] == 'cierto':
            self.valor = True
            p[0] = True
        elif p[1] == 'falso':
            self.valor = False
            p[0] = False
        else:
            self.valor = p[1]
            p[0] = p[1]

    def p_expression_group(self, p):
        '''operando : '(' expression ')' '''
        p[0] = p[2]
    
    def p_expression_operando_signo(self, p):
        '''operando : '+' operando
                    | '-' operando'''
        if p[1] == '+':
            p[0] = +p[2]
        elif p[1] == '-':
            p[0] = -p[2]
    
    def p_operando_vector(self,p):
        '''operando : NAME '[' NUMBER ']' '''
        if p[1] in self.vectors:
            j = 0
            if p[3] > self.vectors[p[1]]['tamaño']:
                print("ERROR: Indice fuera de rango")
            else:
                for elem in self.lista_vectores:
                    if self.lista_vectores[j]['nombre_vector'] == p[1]:
                        p[0] = self.lista_vectores[j]['valores'][p[3]]
                        j += 1
        else:
            print("ERROR: Se intenta acceder a un vector no declarado")

    def p_operando_long(self,p):
        '''operando : NAME '.' operando
                    | LONG '''

        if p[1] not in self.names and p[1] in self.vectors:
            p[0] = self.vectors[p[1]]['tamaño']
        elif p[1] not in self.vectors and p[1] != 'long':
            print("ERROR: Intento de acceso a un vector no declarado")
        elif p[1] in self.names:
            print("ERROR: La variable no contiene el atributo 'long' ")

    def p_multiplicador_operando(self, p):
        '''multiplicador : multiplicador '*' operando
                         | multiplicador '/' operando '''
        if p[2] == '*':
            if type(p[1]) is dict or type(p[3]) is dict:
                if (type(p[1]) is dict and p[1]['tipo'] == 'booleano') or (type(p[3]) is dict and p[3]['tipo'] == 'booleano'):
                    print("ERROR: No se pueden realizar operaciones aritméticas con booleanos")
                if (type(p[1]) is dict and p[1]['tipo'] == 'caracter') or (type(p[3]) is dict and p[3]['tipo'] == 'carcater'):
                    print("ERROR: No se pueden realizar multiplicaciones y divisiones con variables de tipo str")
                else:
                    if type(p[1]) is dict and type(p[3]) is not dict:
                        if p[1]['valor'] is None:
                                print("ERROR: No se puede multiplicar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and type(p[3]) is int:
                                p[0] = int(p[1]['valor'] * p[3])
                            elif p[1]['tipo'] == 'real' and type(p[3]) is float:
                                p[0] = float(p[1]['valor'] * p[3])
                    elif type(p[3]) is dict and type(p[1]) is not dict:
                        if p[3]['valor'] is None:
                            print("ERROR: No se puede multiplicar variables con el valor None")
                        else:
                            if p[3]['tipo'] == 'entero' and type(p[1]) is int:
                                p[0] = int(p[1] * p[3]['valor'])
                            elif p[3]['tipo'] == 'real' and type(p[1]) is float:
                                p[0] = float(p[1] * p[3]['valor'])
                    elif type(p[1]) is dict and type(p[3]) is dict:
                        if p[1]['valor'] is None or p[3]['valor'] is None:
                            print("ERROR: No se puede smultiplicar variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and p[3]['tipo'] == 'entero':
                                p[0] = int(p[1]['valor'] * p[3]['valor'])
                            elif p[1]['tipo'] == 'real' and p[3]['tipo'] == 'real':
                                p[0] = float(p[1]['valor'] * p[3]['valor'])
            else:
                if type(p[1]) is int and type(p[3]) is int:
                    p[0] = int(p[1] * p[3])
                elif type(p[1]) is float and type(p[3]) is float:
                    p[0] = float(p[1] * p[3])
        elif p[2] == '/':
            if type(p[1]) is dict or type(p[3]) is dict:
                if (type(p[1]) is dict and p[1]['tipo'] == 'booleano') or (type(p[3]) is dict and p[3]['tipo'] == 'booleano' ):
                    print("ERROR: No se pueden realizar operaciones aritméticas con booleanos")
                if (type(p[1]) is dict and p[1]['tipo'] == 'caracter') or (type(p[3]) is dict and p[3]['tipo'] == 'carcater'):
                    print("ERROR: No se pueden realizar multiplicaciones y divisiones con variables de tipo str")
                else:
                    if type(p[1]) is dict and type(p[3]) is not dict:
                        if p[1]['valor'] is None:
                            print("ERROR: No se puede dividir variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and type(p[3]) is int:
                                p[0] = int(p[1]['valor'] / p[3])
                            elif p[1]['tipo'] == 'real' and type(p[3]) is float:
                                p[0] = float(p[1]['valor'] / p[3])
                    elif type(p[3]) is dict and type(p[1]) is not dict:
                        if p[3]['valor'] is None:
                            print("ERROR: No se puede dividir variables con el valor None")
                        else:
                            if p[3]['tipo'] == 'entero' and type(p[1]) is int:
                                p[0] = int(p[1] / p[3]['valor'])
                            elif p[3]['tipo'] == 'real' and type(p[1]) is float:
                                p[0] = float(p[1] / p[3]['valor'])
                    elif type(p[1]) is dict and type(p[3]) is dict:
                        if p[1]['valor'] is None or p[3]['valor'] is None:
                            print("ERROR: No se puede dividir variables con el valor None")
                        else:
                            if p[1]['tipo'] == 'entero' and p[3]['tipo'] == 'entero':
                                p[0] = int(p[1]['valor'] / p[3]['valor'])
                            elif p[1]['tipo'] == 'real' and p[3]['tipo'] == 'real':
                                p[0] = float(p[1]['valor'] / p[3]['valor'])
            else:
                if type(p[1]) is int and type(p[3]) is int:
                    p[0] = int(p[1] / p[3])
                elif type(p[1]) is float and type(p[3]) is float:
                    p[0] = float(p[1] / p[3])

    def p_operando_cient(self, p):
        '''operando : EXPONENCIAL '(' NUMBER ')'
                    | LOGARITMICA '(' NUMBER ')'
                    | SENO '(' NUMBER ')'
                    | COSENO '(' NUMBER ')' '''
        if p[1] == 'exp':
            p[0] = math.exp(float(p[3]))
        elif p[1] == 'log':
            p[0] = math.log10(float(p[3]))
        elif p[1] == 'sin':
            p[0] = math.sin(float(p[3]))
        elif p[1] == 'cos':
            p[0] = math.cos(float(p[3]))

    def p_operando_name(self, p):
        "operando : NAME"
        try:
            p[0] = self.names[p[1]]
        except LookupError:
            print("Undefined name '%s'" % p[1])
            p[0] = p[1]

    def p_error(self, p):
        if p:
            print(p)
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")
    
    def parse(self, s):
        yacc.parse(s)