# -*- coding: utf-8 -*-
# Analizador sintáctico de ViLe
# Marcel Benítez Martínez 1139855
# Abraham Rodríguez

import ply.yacc as yacc
import lexer
from semantics import *
tokens = lexer.tokens

# Regla inicial de programa
def p_program(p):
  '''program : main functionloop'''
  p[0] = "Valid"

# Regla del bloque de main
def p_main(p):
  '''main : MAIN block'''
  add_main_to_dict()


# Regla de loop de funciones
def p_functionloop(p):
  ''' functionloop : function functionloop  
                   |'''

# Regla para definición de funciones
def p_function(p):
  ''' function : FUNCTION functiontype ID O_PARENTHESIS parameters C_PARENTHESIS block'''
  funct_options['id'] = p[3]
  add_funct_to_dict(funct_options['id'], funct_options['type'], funct_options['params'])
  funct_options['params'] = {}


# Regla que define el tipo de función
def p_functiontype(p):
  ''' functiontype : VOID
                   | BOOL
                   | INT
                   | FLOAT
                   | STRING'''
  var_options['scope'] = 'function'
  funct_options['type'] = p[1]

# Regla que contiene los tipos de funciones
def p_type(p):
  ''' type : BOOL
           | INT
           | FLOAT
           | STRING'''
  var_options['type'] = p[1]

# Regla del bloque principal del programa
def p_block(p):
  ''' block : O_BRACKET statutesloop functionreturn C_BRACKET'''

# Regla para que pueda haber un return en una función
def p_functionreturn(p):
  '''functionreturn : RETURN expression SEMICOLON
                    |'''
  clear_var_dict()

# Regla del ciclo de estatutos
def p_statutesloop(p):
  ''' statutesloop : statute statutesloop
                   |'''

# Regla de contiene los tipos de estatutos
def p_statute(p):
  ''' statute : init
              | condition
              | writting
              | loop
              | assignation
              | functioncall'''

# Regla para estatuto de asignación
def p_assignation(p):
  ''' assignation : var_assign EQUALS expression SEMICOLON'''

# Regla de estatuto para escritura
def p_writting(p):
  ''' writting :  PRINT O_PARENTHESIS writtingloop C_PARENTHESIS SEMICOLON'''

# Regla para ciclo de lo que puede ir dentro del print
def p_writtingloop(p):
  ''' writtingloop : expression optionalwritting'''

# Regla para múltiples expresiones en el print
def p_optionalwritting(p):
  ''' optionalwritting : COMMA writtingloop
                       |'''
# Regla de inicialización de variables
def p_init(p):
  ''' init : listinit
           | normalinit'''

# Regla de inicialización de variables normales
def p_normalinit(p):
  ''' normalinit : type var EQUALS expression SEMICOLON'''

# Regla de inicialización de variables tipo lista
def p_listinit(p):
  ''' listinit : LIST type var EQUALS list SEMICOLON'''

# Regla de formato de variable tipo listo
def p_list(p):
  ''' list : O_S_BRACKET listelements C_S_BRACKET'''

# Regla de inicialización de los elementos de una lista
def p_listelements(p):
  ''' listelements : constants optionalconstants 
                   |'''
# Regla de inicialización de más elementos de una lista
def p_optionalconstants(p):
  ''' optionalconstants : COMMA constants optionalconstants
                        |'''

# Regla de estatuto de condición
def p_condition(p):
  ''' condition : IF O_PARENTHESIS expression C_PARENTHESIS block else'''

# Regla para el else del estatuto de condición
def p_else(p):
  ''' else : ELSE block
           |'''

# Las siguientes 4 reglas son para expresiones
def p_expression(p):
  ''' expression : expression2 expressionoptional'''

def p_expressionoptional(p):
  ''' expressionoptional : logicop expression2
                         |'''

def p_expression2(p):
  ''' expression2 : exp expression2optional'''

def p_expression2optional(p):
  ''' expression2optional : relop exp
                          |'''
                          
# Reglas de operadores lógicos
def p_logicop(p):
  ''' logicop : AND
              | OR'''
  operator_stack.append(p[1])
# Reglas de operaciones relacionales
def p_relop(p):
  ''' relop : EQUALITY
            | GREATER
            | GREATER_EQUAL
            | LESS
            | LESS_EQUAL
            | DIFFERENT'''
  operator_stack.append(p[1])

# Regla para expresión
def p_exp(p):
  ''' exp : term exploop'''

# Regla para ciclo de expresión
def p_exploop(p):
  ''' exploop : addsub exp
              |'''
# Regla que tiene operadores de suma y resta
def p_addsub(p):
  ''' addsub : SUM
             | MINUS'''
  operator_stack.append(p[1])

# Regla para terminos
def p_term(p):
  ''' term : fact termloop'''

# Regla para ciclo de terminos
def p_termloop(p):
  ''' termloop : divmult term
               |'''

# Regla que tiene los operadores de multiplicación, división, y residuo
def p_divmult(p):
  ''' divmult : MULTIPLY
              | DIVIDE
              | MOD'''
  operator_stack.append(p[1])

# Regla para factores
def p_fact(p):
  ''' fact : varconst
           | O_PARENTHESIS add_o_parenthesis expression C_PARENTHESIS add_c_parenthesis'''

def p_add_o_parenthesis(p):
  ''' add_o_parenthesis :'''
  operator_stack.append(p[-1])

def p_add_c_parenthesis(p):
  ''' add_c_parenthesis :'''
  operator_stack.append(p[-1])

def p_var_assign(p):
  ''' var_assign : ID listaccess'''
  operand_stack.append(var_dict[var_options['scope']][p[1]]['address'])
  types_stack.append(var_dict[var_options['scope']][p[1]]['type'])

# Regla para las variables
def p_var(p):
  ''' var : ID listaccess'''
  var_options['id'] = p[1]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_var_to_dict(var_options['id'], var_options['type'], var_options['scope'])
    operand_stack.append(var_dict[var_options['scope']][p[1]]['address'])
    types_stack.append(types[var_options['type']])

# Regla para cuando se accesara una variable de tipo lista
def p_listaccess(p):
  ''' listaccess : O_S_BRACKET INTCONST C_S_BRACKET
                 |'''
# Regla para variables o constantes
def p_varconst(p):
  ''' varconst : varconstfunction
               | constants'''

def p_varconstfunction(p):
  ''' varconstfunction : ID functionorlist'''

def p_functionorlist(p):
  ''' functionorlist : O_S_BRACKET INTCONST C_S_BRACKET
                     | O_PARENTHESIS parametersinput C_PARENTHESIS
                     |'''

# Regla para constantes
def p_constants(p):
  ''' constants : INTCONST
                | FLOATCONST
                | STRINGCONST
                | booleanconst'''

#Regla de constante booleana
def p_booleanconst(p):
  ''' booleanconst : TRUE
                   | FALSE'''

# Regla para ciclos
def p_loop(p):
  ''' loop : whileloop
           | timesloop'''

# Regla para while
def p_whileloop(p):
  ''' whileloop : WHILE O_PARENTHESIS expression C_PARENTHESIS block'''

# Regla para times
def p_timesloop(p):
  ''' timesloop : TIMES O_PARENTHESIS INTCONST C_PARENTHESIS block'''

# Regla de llamada de función
def p_functioncall(p):
  ''' functioncall : ID O_PARENTHESIS parametersinput C_PARENTHESIS SEMICOLON'''

# Regla para parametros de la función en input
def p_parametersinput(p):
  ''' parametersinput : expression parametersinputloop
                      |'''

# Regla para ciclo de ingresar parametros a una función en input
def p_parametersinputloop(p):
  ''' parametersinputloop : COMMA expression parametersinputloop
                         |'''

# Regla para parametros de una función
def p_parameters(p):
  ''' parameters : parameterinit parametersloop
                 |'''

def p_parameterinit(p):
  ''' parameterinit : type ID '''
  var_options['id'] = p[2]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_var_to_dict(var_options['id'], var_options['type'], var_options['scope'])
    funct_options['params'][var_options['id']] = types[var_options['type']]

# Regal para el ciclio de ingresar más parametros a uan función
def p_parametersloop(p):
  ''' parametersloop : COMMA parameterinit parametersloop
                     |'''

# Función de error del parser
def p_error(p):
    if type(p).__name__ == 'NoneType':
      print('Syntax error')
    else:
      print('Syntax error before', p.value, 'at ', p.lineno - 1)
      p.lineno = 0

# Build the parser
parser = yacc.yacc(start='program')

# Main del parser
def check(filename):
  f = open(filename, 'r')
  data = f.read()
  f.close()
  if parser.parse(data) == 'Valid':
    print('VALID!')
    print(operator_stack)
    print(operand_stack)
    print(types_stack)
  exit(0);
  