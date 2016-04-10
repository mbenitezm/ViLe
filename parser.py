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
  ''' function : FUNCTION function_head function_end'''
  add_funct_to_dict(funct_options['id'], funct_options['type'], funct_options['params'], funct_options['params_order'])
  funct_options['id'] = None
  funct_options['type'] = None
  funct_options['params'] = {}
  funct_options['params_order'] = ''


# Regla que define el tipo de función
def p_function_head(p):
  ''' function_head : VOID function_def
                   | BOOL function_with_return_def
                   | INT function_with_return_def
                   | FLOAT function_with_return_def
                   | STRING function_with_return_def'''
  var_options['scope'] = 'function'
  funct_options['type'] = p[1]

# Regla que define una funcion
def p_function_with_return_def(p):
  ''' function_with_return_def : ID O_PARENTHESIS parameters C_PARENTHESIS functionblock'''
  funct_options['id'] = p[1]

def p_function_def(p):
  ''' function_def : ID O_PARENTHESIS parameters C_PARENTHESIS block'''
  funct_options['id'] = p[1]

# Regla que contiene los tipos de variables
def p_type(p):
  ''' type : BOOL
           | INT
           | FLOAT
           | STRING'''
  var_options['type'] = p[1]

# Regla que contiene los tipos de los parametros de las funciones para poderlos
# agregar al orden de parametros
def p_parametertype(p):
  ''' parametertype : BOOL
                    | INT
                    | FLOAT
                    | STRING'''
  var_options['type'] = p[1]
  funct_options['params_order'] = funct_options['params_order'] + str(types[p[1]])

# Regla del bloque principal del programa
def p_block(p):
  ''' block : O_BRACKET statutesloop C_BRACKET'''

# Regla del bloque de las funciones
def p_functionblock(p):
  ''' functionblock : O_BRACKET statutesloop functionreturn C_BRACKET'''

# Regla para que pueda haber un return en una función
def p_functionreturn(p):
  '''functionreturn : RETURN O_BRACKET expression C_BRACKET SEMICOLON
                    | RETURN expression SEMICOLON'''

def p_function_end(p):
  '''function_end : '''
  check_function_return();
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
  ''' assignation : var_assign EQUALS add_equals expression equals_quadruple SEMICOLON'''


# Regla de estatuto para escritura
def p_writting(p):
  ''' writting :  PRINT O_PARENTHESIS writtingloop C_PARENTHESIS SEMICOLON'''

def p_start_printing(p):
  ''' start_printing : '''
  operator_stack.append('print')

def p_print_quadruple(p):
  ''' print_quadruple : '''
  if len(operator_stack) > 0:
    while operator_stack[len(operator_stack)-1] == 'print':
      generate_print_quadruples()
      if len(operator_stack) == 0:
        break

# Regla para ciclo de lo que puede ir dentro del print
def p_writtingloop(p):
  ''' writtingloop : start_printing expression print_quadruple optionalwritting'''

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
  ''' normalinit : type var EQUALS add_equals expression equals_quadruple SEMICOLON'''

def p_equals_quadruple(p):
  ''' equals_quadruple : '''
  if len(operator_stack) > 0:
    while operator_stack[len(operator_stack)-1] == '=':
      generate_equals_quadruples()
      if len(operator_stack) == 0:
        break


def p_add_equals(p):
  ''' add_equals :'''
  operator_stack.append(p[-1])

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
  ''' condition : IF O_PARENTHESIS expression C_PARENTHESIS start_condition block else end_condition'''

# Regla para el else del estatuto de condición
def p_else(p):
  ''' else : ELSE else_condition block
           | '''

def p_start_condition(p):
  '''start_condition :'''
  generate_condition_if_quadruples()

def p_else_condition(p):
  '''else_condition :'''
  generate_condition_else_quadruples()

def p_end_condition(p):
  '''end_condition :'''
  generate_condition_end_quadruples()
  
# Las siguientes 4 reglas son para expresiones
def p_expression(p):
  ''' expression : expression2 expressionoptional'''

def p_expressionoptional(p):
  ''' expressionoptional : logicop expression2 logic_op_quadruple
                         |'''

def p_expression2(p):
  ''' expression2 : exp expression2optional'''

def p_expression2optional(p):
  ''' expression2optional : relop exp relop_quadruple
                          |'''
                          
# Reglas de operadores lógicos
def p_logicop(p):
  ''' logicop : AND
              | OR'''
  operator_stack.append(p[1])

def p_logic_op_quadruple(p):
  '''logic_op_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == 'and' or operator_stack[len(operator_stack)-1] == 'or':
      generate_operations_quadruples()

# Reglas de operaciones relacionales
def p_relop(p):
  ''' relop : EQUALITY
            | GREATER
            | GREATER_EQUAL
            | LESS
            | LESS_EQUAL
            | DIFFERENT'''
  operator_stack.append(p[1])

def p_relop_quadruple(p):
  '''relop_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '>' or operator_stack[len(operator_stack)-1] == '<' or operator_stack[len(operator_stack)-1] == '>=' or operator_stack[len(operator_stack)-1] == '<=' or operator_stack[len(operator_stack)-1] == '!=' or operator_stack[len(operator_stack)-1] == '==':
      generate_operations_quadruples()

# Regla para expresión
def p_exp(p):
  ''' exp : term exp_quadruple exploop'''

def p_exp_quadruple(p):
  ''' exp_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '+' or operator_stack[len(operator_stack)-1] == '-':
      generate_operations_quadruples()

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
  ''' term : fact term_quadruple termloop'''

def p_term_quadruple(p):
  ''' term_quadruple : '''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '*' or operator_stack[len(operator_stack)-1] == '/' or operator_stack[len(operator_stack)-1] == '%':
      generate_operations_quadruples()

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
  operator_stack.pop()

def p_var_assign(p):
  ''' var_assign : ID add_to_stack listaccess'''
  # try:
  #   print_var_dict()
  #   print(var_options['scope'])
  #   operand_stack.append(var_dict[var_options['scope']][p[1]]['address'])
  #   types_stack.append(var_dict[var_options['scope']][p[1]]['type'])
  # except:
  #   print "Variable", p[1], "doesn't exists"
  #   exit(0)

# Regla para las variables
def p_var(p):
  ''' var : ID listaccess'''
  var_options['id'] = p[1]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_var_to_dict(var_options['id'], var_options['type'], var_options['scope'])
    try: 
      operand_stack.append(var_dict[var_options['scope']][p[1]]['address'])
      types_stack.append(types[var_options['type']])
    except:
      print "Variable", p[1], "doesn't exists in line .", p.lineno 
      exit(0)

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

def p_add_to_stack(p):
  ''' add_to_stack : '''
  semantics_add_to_stack(p[-1])

def p_functionorlist(p):
  ''' functionorlist : O_S_BRACKET INTCONST C_S_BRACKET
                     | O_PARENTHESIS parametersinput C_PARENTHESIS
                     | add_to_stack'''

# Regla para constantes
def p_constants(p):
  ''' constants : INTCONST add_int_constant_to_dict
                | FLOATCONST add_float_constant_to_dict
                | STRINGCONST add_string_constant_to_dict
                | booleanconst '''

#Regla de constante booleana
def p_booleanconst(p):
  ''' booleanconst : TRUE add_bool_constant_to_dict
                   | FALSE add_bool_constant_to_dict'''

def p_add_int_constant_to_dict(p):
  ''' add_int_constant_to_dict : '''
  add_constant_to_dict(p[-1], 'int')

def p_add_float_constant_to_dict(p):
  ''' add_float_constant_to_dict : '''
  add_constant_to_dict(p[-1], 'float')

def p_add_string_constant_to_dict(p):
  ''' add_string_constant_to_dict : '''
  add_constant_to_dict(p[-1], 'string')

def p_add_bool_constant_to_dict(p):
  ''' add_bool_constant_to_dict : '''
  add_constant_to_dict(p[-1], 'bool')

# Regla para ciclos
def p_loop(p):
  ''' loop : whileloop
           | timesloop'''

# Regla para while
def p_whileloop(p):
  ''' whileloop : WHILE start_while O_PARENTHESIS expression C_PARENTHESIS condition_while block end_while'''

def p_start_while(p):
  '''start_while :'''
  generate_while_start_quadruples()

def p_condition_while(p):
  '''condition_while :'''
  generate_while_condition_quadruples()

def p_end_while(p):
  '''end_while :'''
  generate_while_end_quadruples()

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
  ''' parameterinit : parametertype ID '''
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
      print('Syntax error in ', p.value, ' at line ', p.lineno)
      p.lineno = 0

# Build the parser
parser = yacc.yacc(start='program')

# Main del parser
# def check(filename):
#   f = open(filename, 'r')
#   data = f.read()
#   f.close()
#   if parser.parse(data) == 'Valid':
#     print('VALID!')
#     print(operator_stack)
#     print(operand_stack)
#     print(types_stack)
#   exit(0);

def check():
  f = open('test/print.txt', 'r')

  data = f.read()
  f.close()
  if parser.parse(data) == 'Valid':
    print('VALID!')
    print(operator_stack)
    print(operand_stack)
    print(types_stack)
    print(quadruplets)
  exit(0);

