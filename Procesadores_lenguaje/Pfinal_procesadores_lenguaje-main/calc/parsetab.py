
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "AND BOOLEANO CARACTER CHAR CIERTO COSENO DEVOLVER ENTERO ENTONCES EXPONENCIAL FALSO FINMIENTRAS FINSI FUNCION IgualIgual Igualdad LOGARITMICA LONG MIENTRAS MayorIgual MenorIgual NAME NOT NUMBER OR REAL REGISTRO SALTO_LINEA SENO SI SINO VECTORstatements : statement SALTO_LINEA statements\n                      | statement statement : \n\n                     | asignacion\n                     | declaracion\n                     | vectores\n                     | registros \n                     | def_funcion\n                     | uso_funcion\n                     | condicionales\n                     | bucles statement : logicodeclaracion : tipo names\n                       | VECTOR tipo NAME '[' NUMBER ']' \n                       | REGISTRO NAME '{' atributos '}' asignacion : tipo NAME Igualdad logico\n                     | NAME Igualdad logico names : NAME ',' names\n                 | NAME tipo : BOOLEANO\n                | ENTERO\n                | REAL \n                | CARACTER \n                | REGISTRO\n                | VECTOR \n                | NAME vectores : NAME '[' NUMBER ']' Igualdad logico registros : NAME '.' NAME Igualdad logico\n                     | NAME NAME atributos : tipo campos ';' atributos\n                     | tipo campos ';' campos : NAME ',' campos\n                  | NAME def_funcion : FUNCION NAME '(' list_args ')' ':' tipo '{' blq_sentencia DEVOLVER blq_sentencia '}' uso_funcion : NAME '(' argumentos ')' list_args : tipo NAME ',' list_args\n                     | tipo NAME\n                     | empty blq_sentencia : statement SALTO_LINEA blq_sentencia\n                         | statement argumentos : argumentos ',' operando\n                      | operando\n                      | empty condicionales : SI blq_sentencia ENTONCES blq_sentencia FINSI\n                         | SI blq_sentencia ENTONCES blq_sentencia SINO blq_sentencia FINSI bucles : MIENTRAS logico blq_sentencia FINMIENTRAS empty : restriccion : restriccion comparador expression\n                       | expression logico : logico condicion restriccion\n                  | restriccion comparador : IgualIgual\n                      | MenorIgual\n                      | MayorIgual\n                      | Igualdad\n                      | '<'\n                      | '>'  condicion : OR\n                     | AND\n                     | NOT \n                     | '!'\n                     | '&'\n                     | '|' expression : multiplicador multiplicador : operandoexpression : expression '+' multiplicador\n                    | expression '-' multiplicadoroperando : NUMBER\n                    | CHAR\n                    | CIERTO\n                    | FALSO operando : '(' expression ')' operando : '+' operando\n                    | '-' operandooperando : NAME '[' NUMBER ']' operando : NAME '.' operando\n                    | LONG multiplicador : multiplicador '*' operando\n                         | multiplicador '/' operando operando : EXPONENCIAL '(' NUMBER ')'\n                    | LOGARITMICA '(' NUMBER ')'\n                    | SENO '(' NUMBER ')'\n                    | COSENO '(' NUMBER ')' operando : NAME"
    
_lr_action_items = {'SALTO_LINEA':([0,2,3,4,5,6,7,8,9,10,11,13,15,19,21,26,27,30,31,32,33,34,39,47,48,49,61,63,64,76,77,83,86,88,89,96,99,100,102,103,104,105,106,111,112,113,114,116,127,128,129,130,131,133,136,141,142,143,144,145,155,156,158,160,],[-3,39,-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-3,-51,-49,-64,-65,-69,-70,-71,-77,-3,-19,-13,-29,-84,100,-3,-73,-74,-50,-17,-84,-76,-72,-3,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,-46,-80,-81,-82,-83,-28,-15,-75,-44,-3,-27,-14,-45,-3,-3,-34,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,39,47,48,49,61,76,77,82,83,86,88,89,96,102,103,104,105,106,111,112,113,114,116,127,128,129,130,131,133,136,141,142,144,145,155,160,],[-3,0,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-3,-19,-13,-29,-84,-73,-74,-1,-50,-17,-84,-76,-72,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-45,-34,]),'NAME':([0,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,54,55,56,57,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,85,89,94,95,96,98,99,100,102,103,104,105,106,115,117,120,122,128,129,130,131,132,141,143,146,147,148,149,156,158,],[13,47,49,56,-68,58,59,61,13,61,-51,-20,-21,-22,-23,-49,-64,61,61,-65,-69,-70,-71,-77,13,61,-58,-59,-60,-61,-62,-63,61,88,61,-25,93,-26,-24,-84,13,61,-52,-53,-54,-55,-56,-57,61,61,61,61,-73,-74,-50,61,112,-76,56,56,-72,61,13,13,-48,-66,-67,-78,-79,61,61,138,140,-80,-81,-82,-83,61,-75,13,56,138,56,56,13,13,]),'VECTOR':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[14,54,-68,14,-51,-49,-64,-65,-69,-70,-71,-77,14,-84,14,-73,-74,-50,-76,54,54,-72,14,14,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,14,54,54,54,14,14,]),'REGISTRO':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[16,57,-68,16,-51,-49,-64,-65,-69,-70,-71,-77,16,-84,16,-73,-74,-50,-76,57,57,-72,16,16,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,16,57,57,57,16,16,]),'FUNCION':([0,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,96,99,100,102,103,104,105,106,128,129,130,131,141,143,156,158,],[17,-68,17,-51,-49,-64,-65,-69,-70,-71,-77,17,-84,17,-73,-74,-50,-76,-72,17,17,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,17,17,17,]),'SI':([0,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,96,99,100,102,103,104,105,106,128,129,130,131,141,143,156,158,],[19,-68,19,-51,-49,-64,-65,-69,-70,-71,-77,19,-84,19,-73,-74,-50,-76,-72,19,19,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,19,19,19,]),'MIENTRAS':([0,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,96,99,100,102,103,104,105,106,128,129,130,131,141,143,156,158,],[20,-68,20,-51,-49,-64,-65,-69,-70,-71,-77,20,-84,20,-73,-74,-50,-76,-72,20,20,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,20,20,20,]),'BOOLEANO':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[22,22,-68,22,-51,-49,-64,-65,-69,-70,-71,-77,22,-84,22,-73,-74,-50,-76,22,22,-72,22,22,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,22,22,22,22,22,22,]),'ENTERO':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[23,23,-68,23,-51,-49,-64,-65,-69,-70,-71,-77,23,-84,23,-73,-74,-50,-76,23,23,-72,23,23,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,23,23,23,23,23,23,]),'REAL':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[24,24,-68,24,-51,-49,-64,-65,-69,-70,-71,-77,24,-84,24,-73,-74,-50,-76,24,24,-72,24,24,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,24,24,24,24,24,24,]),'CARACTER':([0,14,15,19,21,26,27,30,31,32,33,34,39,61,64,76,77,83,89,94,95,96,99,100,102,103,104,105,106,128,129,130,131,141,143,146,148,149,156,158,],[25,25,-68,25,-51,-49,-64,-65,-69,-70,-71,-77,25,-84,25,-73,-74,-50,-76,25,25,-72,25,25,-48,-66,-67,-78,-79,-80,-81,-82,-83,-75,25,25,25,25,25,25,]),'NUMBER':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,51,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,83,84,89,96,97,98,99,100,102,103,104,105,106,115,117,118,128,129,130,131,132,141,143,156,158,],[15,-68,15,15,15,-51,-49,-64,15,15,-65,-69,-70,-71,-77,15,15,-58,-59,-60,-61,-62,-63,15,87,15,15,-84,15,15,-52,-53,-54,-55,-56,-57,15,15,15,15,-73,-74,107,108,109,110,-50,15,-76,-72,124,15,15,15,-48,-66,-67,-78,-79,15,15,135,-80,-81,-82,-83,15,-75,15,15,15,]),'CHAR':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[31,-68,31,31,31,-51,-49,-64,31,31,-65,-69,-70,-71,-77,31,31,-58,-59,-60,-61,-62,-63,31,31,31,-84,31,31,-52,-53,-54,-55,-56,-57,31,31,31,31,-73,-74,-50,31,-76,-72,31,31,31,-48,-66,-67,-78,-79,31,31,-80,-81,-82,-83,31,-75,31,31,31,]),'CIERTO':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[32,-68,32,32,32,-51,-49,-64,32,32,-65,-69,-70,-71,-77,32,32,-58,-59,-60,-61,-62,-63,32,32,32,-84,32,32,-52,-53,-54,-55,-56,-57,32,32,32,32,-73,-74,-50,32,-76,-72,32,32,32,-48,-66,-67,-78,-79,32,32,-80,-81,-82,-83,32,-75,32,32,32,]),'FALSO':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[33,-68,33,33,33,-51,-49,-64,33,33,-65,-69,-70,-71,-77,33,33,-58,-59,-60,-61,-62,-63,33,33,33,-84,33,33,-52,-53,-54,-55,-56,-57,33,33,33,33,-73,-74,-50,33,-76,-72,33,33,33,-48,-66,-67,-78,-79,33,33,-80,-81,-82,-83,33,-75,33,33,33,]),'(':([0,13,15,18,19,20,21,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,50,52,53,59,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[18,53,-68,18,18,18,-51,-49,-64,18,18,-65,-69,-70,-71,-77,78,79,80,81,18,18,-58,-59,-60,-61,-62,-63,18,18,18,95,-84,18,18,-52,-53,-54,-55,-56,-57,18,18,18,18,-73,-74,-50,18,-76,-72,18,18,18,-48,-66,-67,-78,-79,18,18,-80,-81,-82,-83,18,-75,18,18,18,]),'+':([0,13,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,88,89,96,98,99,100,102,103,104,105,106,114,115,117,128,129,130,131,132,141,143,156,158,],[28,-84,-68,28,28,28,-51,72,-64,28,28,-65,-69,-70,-71,-77,28,28,-58,-59,-60,-61,-62,-63,28,28,28,72,-84,28,28,-52,-53,-54,-55,-56,-57,28,28,28,28,-73,-74,-50,28,-84,-76,-72,28,28,28,72,-66,-67,-78,-79,-75,28,28,-80,-81,-82,-83,28,-75,28,28,28,]),'-':([0,13,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,60,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,88,89,96,98,99,100,102,103,104,105,106,114,115,117,128,129,130,131,132,141,143,156,158,],[29,-84,-68,29,29,29,-51,73,-64,29,29,-65,-69,-70,-71,-77,29,29,-58,-59,-60,-61,-62,-63,29,29,29,73,-84,29,29,-52,-53,-54,-55,-56,-57,29,29,29,29,-73,-74,-50,29,-84,-76,-72,29,29,29,73,-66,-67,-78,-79,-75,29,29,-80,-81,-82,-83,29,-75,29,29,29,]),'LONG':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[34,-68,34,34,34,-51,-49,-64,34,34,-65,-69,-70,-71,-77,34,34,-58,-59,-60,-61,-62,-63,34,34,34,-84,34,34,-52,-53,-54,-55,-56,-57,34,34,34,34,-73,-74,-50,34,-76,-72,34,34,34,-48,-66,-67,-78,-79,34,34,-80,-81,-82,-83,34,-75,34,34,34,]),'EXPONENCIAL':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[35,-68,35,35,35,-51,-49,-64,35,35,-65,-69,-70,-71,-77,35,35,-58,-59,-60,-61,-62,-63,35,35,35,-84,35,35,-52,-53,-54,-55,-56,-57,35,35,35,35,-73,-74,-50,35,-76,-72,35,35,35,-48,-66,-67,-78,-79,35,35,-80,-81,-82,-83,35,-75,35,35,35,]),'LOGARITMICA':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[36,-68,36,36,36,-51,-49,-64,36,36,-65,-69,-70,-71,-77,36,36,-58,-59,-60,-61,-62,-63,36,36,36,-84,36,36,-52,-53,-54,-55,-56,-57,36,36,36,36,-73,-74,-50,36,-76,-72,36,36,36,-48,-66,-67,-78,-79,36,36,-80,-81,-82,-83,36,-75,36,36,36,]),'SENO':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[37,-68,37,37,37,-51,-49,-64,37,37,-65,-69,-70,-71,-77,37,37,-58,-59,-60,-61,-62,-63,37,37,37,-84,37,37,-52,-53,-54,-55,-56,-57,37,37,37,37,-73,-74,-50,37,-76,-72,37,37,37,-48,-66,-67,-78,-79,37,37,-80,-81,-82,-83,37,-75,37,37,37,]),'COSENO':([0,15,18,19,20,21,26,27,28,29,30,31,32,33,34,39,40,41,42,43,44,45,46,50,52,53,61,64,65,66,67,68,69,70,71,72,73,74,75,76,77,83,84,89,96,98,99,100,102,103,104,105,106,115,117,128,129,130,131,132,141,143,156,158,],[38,-68,38,38,38,-51,-49,-64,38,38,-65,-69,-70,-71,-77,38,38,-58,-59,-60,-61,-62,-63,38,38,38,-84,38,38,-52,-53,-54,-55,-56,-57,38,38,38,38,-73,-74,-50,38,-76,-72,38,38,38,-48,-66,-67,-78,-79,38,38,-80,-81,-82,-83,38,-75,38,38,38,]),'ENTONCES':([3,4,5,6,7,8,9,10,11,13,15,19,21,26,27,30,31,32,33,34,47,48,49,61,62,63,76,77,83,86,88,89,96,100,102,103,104,105,106,111,112,113,114,116,126,127,128,129,130,131,133,136,141,142,144,145,155,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-3,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,99,-40,-73,-74,-50,-17,-84,-76,-72,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-45,-34,]),'FINMIENTRAS':([3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,47,48,49,61,63,64,76,77,83,86,88,89,96,100,101,102,103,104,105,106,111,112,113,114,116,126,127,128,129,130,131,133,136,141,142,144,145,155,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,-40,-3,-73,-74,-50,-17,-84,-76,-72,-3,127,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-45,-34,]),'FINSI':([3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,47,48,49,61,63,76,77,83,86,88,89,96,99,100,102,103,104,105,106,111,112,113,114,116,125,126,127,128,129,130,131,133,136,141,142,143,144,145,150,155,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,-40,-73,-74,-50,-17,-84,-76,-72,-3,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,142,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-3,-27,-14,155,-45,-34,]),'SINO':([3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,47,48,49,61,63,76,77,83,86,88,89,96,99,100,102,103,104,105,106,111,112,113,114,116,125,126,127,128,129,130,131,133,136,141,142,144,145,155,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,-40,-73,-74,-50,-17,-84,-76,-72,-3,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,143,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-45,-34,]),'DEVOLVER':([3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,47,48,49,61,63,76,77,83,86,88,89,96,100,102,103,104,105,106,111,112,113,114,116,126,127,128,129,130,131,133,136,141,142,144,145,155,156,157,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,-40,-73,-74,-50,-17,-84,-76,-72,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-45,-3,158,-34,]),'}':([3,4,5,6,7,8,9,10,11,13,15,21,26,27,30,31,32,33,34,47,48,49,61,63,76,77,83,86,88,89,96,100,102,103,104,105,106,111,112,113,114,116,119,126,127,128,129,130,131,133,136,141,142,144,145,146,151,155,158,159,160,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-19,-13,-29,-84,-40,-73,-74,-50,-17,-84,-76,-72,-3,-48,-66,-67,-78,-79,-16,-19,-18,-75,-35,136,-39,-46,-80,-81,-82,-83,-28,-15,-75,-44,-27,-14,-31,-30,-45,-3,160,-34,]),'OR':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[41,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,41,-73,-74,-50,41,-84,-76,-72,-48,-66,-67,-78,-79,41,-75,-80,-81,-82,-83,41,-75,41,]),'AND':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[42,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,42,-73,-74,-50,42,-84,-76,-72,-48,-66,-67,-78,-79,42,-75,-80,-81,-82,-83,42,-75,42,]),'NOT':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[43,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,43,-73,-74,-50,43,-84,-76,-72,-48,-66,-67,-78,-79,43,-75,-80,-81,-82,-83,43,-75,43,]),'!':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[44,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,44,-73,-74,-50,44,-84,-76,-72,-48,-66,-67,-78,-79,44,-75,-80,-81,-82,-83,44,-75,44,]),'&':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[45,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,45,-73,-74,-50,45,-84,-76,-72,-48,-66,-67,-78,-79,45,-75,-80,-81,-82,-83,45,-75,45,]),'|':([11,13,15,21,26,27,30,31,32,33,34,61,64,76,77,83,86,88,89,96,102,103,104,105,106,111,114,128,129,130,131,133,141,144,],[46,-84,-68,-51,-49,-64,-65,-69,-70,-71,-77,-84,46,-73,-74,-50,46,-84,-76,-72,-48,-66,-67,-78,-79,46,-75,-80,-81,-82,-83,46,-75,46,]),'Igualdad':([13,15,21,26,27,30,31,32,33,34,47,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[50,-68,69,-49,-64,-65,-69,-70,-71,-77,84,-84,-73,-74,69,115,-76,-72,-48,-66,-67,-78,-79,132,-80,-81,-82,-83,-75,]),'[':([13,61,88,93,],[51,97,97,118,]),'.':([13,61,88,],[52,98,98,]),'*':([13,15,27,30,31,32,33,34,61,76,77,88,89,96,103,104,105,106,114,128,129,130,131,141,],[-84,-68,74,-65,-69,-70,-71,-77,-84,-73,-74,-84,-76,-72,74,74,-78,-79,-75,-80,-81,-82,-83,-75,]),'/':([13,15,27,30,31,32,33,34,61,76,77,88,89,96,103,104,105,106,114,128,129,130,131,141,],[-84,-68,75,-65,-69,-70,-71,-77,-84,-73,-74,-84,-76,-72,75,75,-78,-79,-75,-80,-81,-82,-83,-75,]),'IgualIgual':([13,15,21,26,27,30,31,32,33,34,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[-84,-68,66,-49,-64,-65,-69,-70,-71,-77,-84,-73,-74,66,-84,-76,-72,-48,-66,-67,-78,-79,-75,-80,-81,-82,-83,-75,]),'MenorIgual':([13,15,21,26,27,30,31,32,33,34,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[-84,-68,67,-49,-64,-65,-69,-70,-71,-77,-84,-73,-74,67,-84,-76,-72,-48,-66,-67,-78,-79,-75,-80,-81,-82,-83,-75,]),'MayorIgual':([13,15,21,26,27,30,31,32,33,34,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[-84,-68,68,-49,-64,-65,-69,-70,-71,-77,-84,-73,-74,68,-84,-76,-72,-48,-66,-67,-78,-79,-75,-80,-81,-82,-83,-75,]),'<':([13,15,21,26,27,30,31,32,33,34,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[-84,-68,70,-49,-64,-65,-69,-70,-71,-77,-84,-73,-74,70,-84,-76,-72,-48,-66,-67,-78,-79,-75,-80,-81,-82,-83,-75,]),'>':([13,15,21,26,27,30,31,32,33,34,61,76,77,83,88,89,96,102,103,104,105,106,114,128,129,130,131,141,],[-84,-68,71,-49,-64,-65,-69,-70,-71,-77,-84,-73,-74,71,-84,-76,-72,-48,-66,-67,-78,-79,-75,-80,-81,-82,-83,-75,]),')':([15,27,30,31,32,33,34,53,60,61,76,77,89,90,91,92,95,96,103,104,105,106,107,108,109,110,121,123,128,129,130,131,134,140,141,149,154,],[-68,-64,-65,-69,-70,-71,-77,-47,96,-84,-73,-74,-76,116,-42,-43,-47,-72,-66,-67,-78,-79,128,129,130,131,139,-38,-80,-81,-82,-83,-41,-37,-75,-47,-36,]),',':([15,31,32,33,34,47,53,61,76,77,89,90,91,92,96,112,128,129,130,131,134,138,140,141,],[-68,-69,-70,-71,-77,85,-47,-84,-73,-74,-76,117,-42,-43,-72,85,-80,-81,-82,-83,-41,147,149,-75,]),'{':([22,23,24,25,54,56,57,58,153,],[-20,-21,-22,-23,-25,-26,-24,94,156,]),']':([87,124,135,],[114,141,145,]),';':([137,138,152,],[146,-33,-32,]),':':([139,],[148,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,39,],[1,82,]),'statement':([0,19,39,64,99,100,143,156,158,],[2,63,2,63,63,63,63,63,63,]),'asignacion':([0,19,39,64,99,100,143,156,158,],[3,3,3,3,3,3,3,3,3,]),'declaracion':([0,19,39,64,99,100,143,156,158,],[4,4,4,4,4,4,4,4,4,]),'vectores':([0,19,39,64,99,100,143,156,158,],[5,5,5,5,5,5,5,5,5,]),'registros':([0,19,39,64,99,100,143,156,158,],[6,6,6,6,6,6,6,6,6,]),'def_funcion':([0,19,39,64,99,100,143,156,158,],[7,7,7,7,7,7,7,7,7,]),'uso_funcion':([0,19,39,64,99,100,143,156,158,],[8,8,8,8,8,8,8,8,8,]),'condicionales':([0,19,39,64,99,100,143,156,158,],[9,9,9,9,9,9,9,9,9,]),'bucles':([0,19,39,64,99,100,143,156,158,],[10,10,10,10,10,10,10,10,10,]),'logico':([0,19,20,39,50,64,84,99,100,115,132,143,156,158,],[11,11,64,11,86,11,111,11,11,133,144,11,11,11,]),'tipo':([0,14,19,39,64,94,95,99,100,143,146,148,149,156,158,],[12,55,12,12,12,120,122,12,12,12,120,153,122,12,12,]),'restriccion':([0,19,20,39,40,50,64,84,99,100,115,132,143,156,158,],[21,21,21,21,83,21,21,21,21,21,21,21,21,21,21,]),'expression':([0,18,19,20,39,40,50,64,65,84,99,100,115,132,143,156,158,],[26,60,26,26,26,26,26,26,102,26,26,26,26,26,26,26,26,]),'multiplicador':([0,18,19,20,39,40,50,64,65,72,73,84,99,100,115,132,143,156,158,],[27,27,27,27,27,27,27,27,27,103,104,27,27,27,27,27,27,27,27,]),'operando':([0,18,19,20,28,29,39,40,50,52,53,64,65,72,73,74,75,84,98,99,100,115,117,132,143,156,158,],[30,30,30,30,76,77,30,30,30,89,91,30,30,30,30,105,106,30,89,30,30,30,134,30,30,30,30,]),'condicion':([11,64,86,111,133,144,],[40,40,40,40,40,40,]),'names':([12,85,],[48,113,]),'blq_sentencia':([19,64,99,100,143,156,158,],[62,101,125,126,150,157,159,]),'comparador':([21,83,],[65,65,]),'argumentos':([53,],[90,]),'empty':([53,95,149,],[92,123,123,]),'atributos':([94,146,],[119,151,]),'list_args':([95,149,],[121,154,]),'campos':([120,147,],[137,152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statement SALTO_LINEA statements','statements',3,'p_statements','myParser.py',43),
  ('statements -> statement','statements',1,'p_statements','myParser.py',44),
  ('statement -> <empty>','statement',0,'p_statement_salto_linea','myParser.py',47),
  ('statement -> asignacion','statement',1,'p_statement_salto_linea','myParser.py',49),
  ('statement -> declaracion','statement',1,'p_statement_salto_linea','myParser.py',50),
  ('statement -> vectores','statement',1,'p_statement_salto_linea','myParser.py',51),
  ('statement -> registros','statement',1,'p_statement_salto_linea','myParser.py',52),
  ('statement -> def_funcion','statement',1,'p_statement_salto_linea','myParser.py',53),
  ('statement -> uso_funcion','statement',1,'p_statement_salto_linea','myParser.py',54),
  ('statement -> condicionales','statement',1,'p_statement_salto_linea','myParser.py',55),
  ('statement -> bucles','statement',1,'p_statement_salto_linea','myParser.py',56),
  ('statement -> logico','statement',1,'p_statement_expr','myParser.py',74),
  ('declaracion -> tipo names','declaracion',2,'p_declaracion','myParser.py',80),
  ('declaracion -> VECTOR tipo NAME [ NUMBER ]','declaracion',6,'p_declaracion','myParser.py',81),
  ('declaracion -> REGISTRO NAME { atributos }','declaracion',5,'p_declaracion','myParser.py',82),
  ('asignacion -> tipo NAME Igualdad logico','asignacion',4,'p_asignacion_assign','myParser.py',112),
  ('asignacion -> NAME Igualdad logico','asignacion',3,'p_asignacion_assign','myParser.py',113),
  ('names -> NAME , names','names',3,'p_names_name','myParser.py',132),
  ('names -> NAME','names',1,'p_names_name','myParser.py',133),
  ('tipo -> BOOLEANO','tipo',1,'p_tipo_tipos','myParser.py',144),
  ('tipo -> ENTERO','tipo',1,'p_tipo_tipos','myParser.py',145),
  ('tipo -> REAL','tipo',1,'p_tipo_tipos','myParser.py',146),
  ('tipo -> CARACTER','tipo',1,'p_tipo_tipos','myParser.py',147),
  ('tipo -> REGISTRO','tipo',1,'p_tipo_tipos','myParser.py',148),
  ('tipo -> VECTOR','tipo',1,'p_tipo_tipos','myParser.py',149),
  ('tipo -> NAME','tipo',1,'p_tipo_tipos','myParser.py',150),
  ('vectores -> NAME [ NUMBER ] Igualdad logico','vectores',6,'p_vectores_vector','myParser.py',156),
  ('registros -> NAME . NAME Igualdad logico','registros',5,'p_registros_registro','myParser.py',174),
  ('registros -> NAME NAME','registros',2,'p_registros_registro','myParser.py',175),
  ('atributos -> tipo campos ; atributos','atributos',4,'p_atributos','myParser.py',194),
  ('atributos -> tipo campos ;','atributos',3,'p_atributos','myParser.py',195),
  ('campos -> NAME , campos','campos',3,'p_campos','myParser.py',199),
  ('campos -> NAME','campos',1,'p_campos','myParser.py',200),
  ('def_funcion -> FUNCION NAME ( list_args ) : tipo { blq_sentencia DEVOLVER blq_sentencia }','def_funcion',12,'p_deffunc_funcion','myParser.py',213),
  ('uso_funcion -> NAME ( argumentos )','uso_funcion',4,'p_usofunc_funcion','myParser.py',222),
  ('list_args -> tipo NAME , list_args','list_args',4,'p_listargs_sentencia','myParser.py',229),
  ('list_args -> tipo NAME','list_args',2,'p_listargs_sentencia','myParser.py',230),
  ('list_args -> empty','list_args',1,'p_listargs_sentencia','myParser.py',231),
  ('blq_sentencia -> statement SALTO_LINEA blq_sentencia','blq_sentencia',3,'p_blq_sentencias','myParser.py',245),
  ('blq_sentencia -> statement','blq_sentencia',1,'p_blq_sentencias','myParser.py',246),
  ('argumentos -> argumentos , operando','argumentos',3,'p_argumentos','myParser.py',250),
  ('argumentos -> operando','argumentos',1,'p_argumentos','myParser.py',251),
  ('argumentos -> empty','argumentos',1,'p_argumentos','myParser.py',252),
  ('condicionales -> SI blq_sentencia ENTONCES blq_sentencia FINSI','condicionales',5,'p_condicionales','myParser.py',257),
  ('condicionales -> SI blq_sentencia ENTONCES blq_sentencia SINO blq_sentencia FINSI','condicionales',7,'p_condicionales','myParser.py',258),
  ('bucles -> MIENTRAS logico blq_sentencia FINMIENTRAS','bucles',4,'p_bucles','myParser.py',261),
  ('empty -> <empty>','empty',0,'p_empty','myParser.py',264),
  ('restriccion -> restriccion comparador expression','restriccion',3,'p_restriccion','myParser.py',269),
  ('restriccion -> expression','restriccion',1,'p_restriccion','myParser.py',270),
  ('logico -> logico condicion restriccion','logico',3,'p_logico','myParser.py',441),
  ('logico -> restriccion','logico',1,'p_logico','myParser.py',442),
  ('comparador -> IgualIgual','comparador',1,'p_comparador','myParser.py',446),
  ('comparador -> MenorIgual','comparador',1,'p_comparador','myParser.py',447),
  ('comparador -> MayorIgual','comparador',1,'p_comparador','myParser.py',448),
  ('comparador -> Igualdad','comparador',1,'p_comparador','myParser.py',449),
  ('comparador -> <','comparador',1,'p_comparador','myParser.py',450),
  ('comparador -> >','comparador',1,'p_comparador','myParser.py',451),
  ('condicion -> OR','condicion',1,'p_condicion','myParser.py',455),
  ('condicion -> AND','condicion',1,'p_condicion','myParser.py',456),
  ('condicion -> NOT','condicion',1,'p_condicion','myParser.py',457),
  ('condicion -> !','condicion',1,'p_condicion','myParser.py',458),
  ('condicion -> &','condicion',1,'p_condicion','myParser.py',459),
  ('condicion -> |','condicion',1,'p_condicion','myParser.py',460),
  ('expression -> multiplicador','expression',1,'p_expression_multiplicador','myParser.py',465),
  ('multiplicador -> operando','multiplicador',1,'p_multiplicador','myParser.py',469),
  ('expression -> expression + multiplicador','expression',3,'p_expression_binop','myParser.py',473),
  ('expression -> expression - multiplicador','expression',3,'p_expression_binop','myParser.py',474),
  ('operando -> NUMBER','operando',1,'p_expression_operando_number','myParser.py',561),
  ('operando -> CHAR','operando',1,'p_expression_operando_number','myParser.py',562),
  ('operando -> CIERTO','operando',1,'p_expression_operando_number','myParser.py',563),
  ('operando -> FALSO','operando',1,'p_expression_operando_number','myParser.py',564),
  ('operando -> ( expression )','operando',3,'p_expression_group','myParser.py',576),
  ('operando -> + operando','operando',2,'p_expression_operando_signo','myParser.py',580),
  ('operando -> - operando','operando',2,'p_expression_operando_signo','myParser.py',581),
  ('operando -> NAME [ NUMBER ]','operando',4,'p_operando_vector','myParser.py',588),
  ('operando -> NAME . operando','operando',3,'p_operando_long','myParser.py',602),
  ('operando -> LONG','operando',1,'p_operando_long','myParser.py',603),
  ('multiplicador -> multiplicador * operando','multiplicador',3,'p_multiplicador_operando','myParser.py',613),
  ('multiplicador -> multiplicador / operando','multiplicador',3,'p_multiplicador_operando','myParser.py',614),
  ('operando -> EXPONENCIAL ( NUMBER )','operando',4,'p_operando_cient','myParser.py',689),
  ('operando -> LOGARITMICA ( NUMBER )','operando',4,'p_operando_cient','myParser.py',690),
  ('operando -> SENO ( NUMBER )','operando',4,'p_operando_cient','myParser.py',691),
  ('operando -> COSENO ( NUMBER )','operando',4,'p_operando_cient','myParser.py',692),
  ('operando -> NAME','operando',1,'p_operando_name','myParser.py',703),
]
