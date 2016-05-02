# -*- coding: utf-8 -*-
# Analizador sintáctico de ViLe
# Marcel Benítez Martínez 1139855
# Abraham Rodríguez 1195653

import ply.yacc as yacc
import lexer
import sys
from semantics import *
from vm import *
tokens = lexer.tokens

# Regla inicial de programa
def p_program(p):
  '''program : generate_main_goto functionloop fill_main_goto main generate_end_all global_memory_needed'''
  p[0] = "Valid"

# Regla que calcula la memoria necesitada por la memoria global
def p_global_memory_needed(p):
  '''global_memory_needed : '''
  get_global_memory_needed()

# Llamar a función semántica para general cuádruplo de finalización
def p_generate_end_all(p):
  '''generate_end_all :'''
  generate_end_all_quadruple()

# Llamar a función semántica para cuádruplo de ir al main
def p_generate_main_goto(p):
  ''' generate_main_goto : '''
  generate_main_goto()

# Llamar a función semántica para llenar el salto del goto main
def p_fill_main_goto(p):
  ''' fill_main_goto : '''
  fill_main_goto()

# Regla del bloque de main
def p_main(p):
  '''main : MAIN start_main block'''
  add_main_to_dict()

# Prende la bandera de las opciones para indicar que se encuentrae en el main
def p_start_main(p):
  ''' start_main : '''
  start_main()

# Regla de loop de funciones
def p_functionloop(p):
  ''' functionloop : function functionloop  
                   |'''

# Regla para definición de funciones
def p_function(p):
  ''' function : FUNCTION function_head function_end'''
  update_funct_memory(funct_options['id'], get_memory_needed_for_function())
  funct_options['id'] = None
  funct_options['start'] = None
  funct_options['type'] = None
  funct_options['params'] = []
  funct_options['params_order'] = ''
  current_function['id'] = None
  current_function['type'] = None
  current_function['return'] = False
  release_fun_temp_memory()

# Agrega al diccionario de funciones el cuádruplo de inicio de la función
def p_add_function_init_to_dict(p):
  '''add_function_init_to_dict : '''
  add_funct_to_dict(funct_options['id'], funct_options['type'], funct_options['params'], funct_options['params_order'], funct_options['start'], get_memory_needed_for_function())


# Regla que define el tipo de función
def p_function_head(p):
  ''' function_head : VOID add_function_type_to_options function_def
                   | BOOL add_function_type_to_options function_with_return_def
                   | INT add_function_type_to_options function_with_return_def
                   | FLOAT add_function_type_to_options function_with_return_def
                   | STRING add_function_type_to_options function_with_return_def'''
  var_options['scope'] = 'function'

# Al diccionario de opciones de fucnión le indica el tipo de función
def p_add_function_type_to_options(p):
  '''add_function_type_to_options : '''
  funct_options['type'] = p[-1]

# Regla que define una funcion
def p_function_with_return_def(p):
  ''' function_with_return_def : ID add_function_id_to_options add_function_to_global_variables check_current_quadruple O_PARENTHESIS parameters C_PARENTHESIS add_function_init_to_dict functionblock '''
  validate_function_return()

# Agrega la función como variable global para la hora de la asignació de retorno
def p_add_function_to_global_variables(p):
  ''' add_function_to_global_variables : '''
  add_function_to_global_variables(funct_options['id'], funct_options['type'])

# Llamar a función semántica para la creación del cuádruplo de return de una función.
def p_function_def(p):
  ''' function_def : ID add_function_id_to_options check_current_quadruple O_PARENTHESIS parameters C_PARENTHESIS add_function_init_to_dict block'''
  create_function_return_quadruple()

# Llamar a función semántica
def p_check_current_quadruple(p):
  '''check_current_quadruple : '''
  funct_options['start'] = get_current_quadruple()

# Registra el id de la funíón en las opciones de la función
def p_add_function_id_to_options(p):
  '''add_function_id_to_options : '''
  funct_options['id'] = p[-1]

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
  ''' functionblock : O_BRACKET functionstatutesloop C_BRACKET'''

# Regla para que pueda haber un return en una función
def p_functionreturn(p):
  '''functionreturn : RETURN add_function_var_to_stack expression SEMICOLON'''
  check_function_return()
  generate_equals_quadruples()
  create_function_return_quadruple()

# Agregar la función al stack (tipo, nombre y operando)
def p_add_function_var_to_stack(p):
  ''' add_function_var_to_stack : '''
  add_function_var_to_stack()

# Despeja el diccionario de variable y llama a función semántica de generación de cuádruplo de finalización de dunciones
def p_function_end(p):
  '''function_end : '''
  create_function_end_quadruple()
  clear_var_dict()

# Regla del ciclo de estatutos
def p_statutesloop(p):
  ''' statutesloop : statute statutesloop
                   |'''

# Regla de ciclo de funciones
def p_functionstatutesloopp(p):
  ''' functionstatutesloop : functionstatute functionstatutesloop
                           | functionreturn
                           |''' 

# Regla de contiene los tipos de estatutos
def p_statute(p):
  ''' statute : init
              | condition
              | writting
              | loop
              | assignation
              | functioncall'''

# Regla para estatuto de funciones
def p_functionstatute(p):
  ''' functionstatute : init
                      | functioncondition
                      | writting
                      | functionloops
                      | assignation
                      | functioncall'''

# Regla para estatuto de asignación
def p_assignation(p):
  ''' assignation : var_assign EQUALS add_equals expression equals_quadruple SEMICOLON'''
  if var_options['scope'] == 'function':
    last_return(False)


# Regla de estatuto para escritura
def p_writting(p):
  ''' writting :  PRINT O_PARENTHESIS writtingloop C_PARENTHESIS SEMICOLON'''
  if var_options['scope'] == 'function':
    last_return(False)

# agrega al stack de operadores el print
def p_start_printing(p):
  ''' start_printing : '''
  operator_stack.append('print')

# Llamar a función semántica para general cuádruplo de print
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
  if var_options['scope'] == 'function':
    last_return(False)

# Regla de inicialización de variables normales
def p_normalinit(p):
  ''' normalinit : type var EQUALS add_equals expression equals_quadruple SEMICOLON'''

# Llamar a función semántica para crear cuádruplo de =
def p_equals_quadruple(p):
  ''' equals_quadruple : '''
  if len(operator_stack) > 0:
    while operator_stack[len(operator_stack)-1] == '=':
      generate_equals_quadruples()
      if len(operator_stack) == 0:
        break

# Agrega al stack de operadores el =
def p_add_equals(p):
  ''' add_equals :'''
  operator_stack.append(p[-1])

# Regla de inicialización de variables tipo lista
def p_listinit(p):
  ''' listinit : LIST type ID EQUALS start_list list SEMICOLON'''
  var_options['id'] = p[3]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_list_to_dict(var_options['id'], var_options['type'], var_options['list'], var_options['size'], var_options['scope'])
    var_options['list'] = False
    var_options['size'] = None

# Regla de formato de variable tipo listo
def p_list(p):
  ''' list : O_S_BRACKET listelements C_S_BRACKET'''

# Regla de inicialización de una lista
def p_start_list(p):
  ''' start_list : '''
  current_list.append({'id' : None , 'start_address' : get_current_memory(var_options['scope'], var_options['type'])})
  var_options['list'] = True
  var_options['size'] = 0

# Regla de inicialización de los elementos de una lista
def p_listelements(p):
  ''' listelements : expression generate_list_assignation optionallist'''


# Regla de inicialización de más elementos de una lista
def p_optionallist(p):
  ''' optionallist : COMMA expression generate_list_assignation optionallist
                   |'''

# Llamar a función semántica para generación de cuadruplos de asignación de lista
def p_generate_list_assignation(p):
  ''' generate_list_assignation : '''
  generate_list_assignation_quadruple()
  var_options['size'] = var_options['size'] + 1


# Regla de estatuto de condición
def p_condition(p):
  ''' condition : IF O_PARENTHESIS expression C_PARENTHESIS start_condition block else end_condition'''

# Regla para la condición de una función
def p_functioncondition(p):
  ''' functioncondition : IF O_PARENTHESIS expression C_PARENTHESIS start_condition functionblock functionelse end_condition'''

# Regla para el else del estatuto de condición
def p_else(p):
  ''' else : ELSE else_condition block
           | '''
# Regla para el else de una condición dentro de una función
def p_functionelse(p):
  ''' functionelse : ELSE else_condition functionblock
                   | '''

# Llamar a función semántica para general cuádruplo de GOTOF
def p_start_condition(p):
  '''start_condition :'''
  generate_condition_if_quadruples()

# Llamar a función semántica para general cuádruplo de GOTO
def p_else_condition(p):
  '''else_condition :'''
  generate_condition_else_quadruples()

# Llamar a función semántica para general cuádruplo de END
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

# Mete al stack de operadores el and u or
def p_logic_op_quadruple(p):
  '''logic_op_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == 'and' or operator_stack[len(operator_stack)-1] == 'or':
      generate_operations_quadruples(var_options['scope'])

# Reglas de operaciones relacionales
def p_relop(p):
  ''' relop : EQUALITY
            | GREATER
            | GREATER_EQUAL
            | LESS
            | LESS_EQUAL
            | DIFFERENT'''
  operator_stack.append(p[1])

# Llamar a función semántica para crear cuádruplo de operadores relacionales
def p_relop_quadruple(p):
  '''relop_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '>' or operator_stack[len(operator_stack)-1] == '<' or operator_stack[len(operator_stack)-1] == '>=' or operator_stack[len(operator_stack)-1] == '<=' or operator_stack[len(operator_stack)-1] == '!=' or operator_stack[len(operator_stack)-1] == '==':
      generate_operations_quadruples(var_options['scope'])

# Regla para expresión
def p_exp(p):
  ''' exp : term exp_quadruple exploop'''

# Llamar a función semántica para crear cuádruplo de operaciones para sumas y restas
def p_exp_quadruple(p):
  ''' exp_quadruple :'''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '+' or operator_stack[len(operator_stack)-1] == '-':
      generate_operations_quadruples(var_options['scope'])

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

# Llamar a función semántica para crear cuádruplo de operaciones para multiplicación, división y mod
def p_term_quadruple(p):
  ''' term_quadruple : '''
  if len(operator_stack) > 0:
    if operator_stack[len(operator_stack)-1] == '*' or operator_stack[len(operator_stack)-1] == '/' or operator_stack[len(operator_stack)-1] == '%':
      generate_operations_quadruples(var_options['scope'])

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

# Agregar fondo falso a pila de operadores
def p_add_o_parenthesis(p):
  ''' add_o_parenthesis :'''
  operator_stack.append(p[-1])

# Quitar fondo falso de pila de operadores
def p_add_c_parenthesis(p):
  ''' add_c_parenthesis :'''
  operator_stack.pop()

# Regla de asignaíón de variables
def p_var_assign(p):
  ''' var_assign : ID listaccess'''
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
  ''' var : ID'''
  var_options['id'] = p[1]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_var_to_dict(var_options['id'], var_options['type'], var_options['list'], var_options['size'], var_options['scope'])
    try: 
      operand_stack.append(var_dict[var_options['scope']][p[1]]['address'])
      types_stack.append(types[var_options['type']])
    except:
      print "Variable", p[1], "doesn't exists in line .", p.lineno 
      exit(0)

# Regla para cuando se accesara una variable de tipo lista
def p_listaccess(p):
  ''' listaccess : add_list_variable add_o_parenthesis O_S_BRACKET expression C_S_BRACKET add_c_parenthesis add_list_index_to_stack
                 | add_to_stack'''

# Agregar a stack el indice de la lista
def p_add_list_index_to_stack(p):
  ''' add_list_index_to_stack : '''
  add_list_index_to_stack()

# Regla para variables o constantes
def p_varconst(p):
  ''' varconst : varconstfunction
               | constants'''

# Regla para llamada a una función
def p_varconstfunction(p):
  ''' varconstfunction : ID functionorlist'''

# Agregar al stack el elemento anterior
def p_add_to_stack(p):
  ''' add_to_stack : '''
  semantics_add_to_stack(p[-1])

# regla para decidir si es una lista o una función
def p_functionorlist(p):
  ''' functionorlist : add_list_variable add_o_parenthesis O_S_BRACKET expression C_S_BRACKET add_c_parenthesis add_list_index_to_stack
                     | add_o_parenthesis check_function_exists O_PARENTHESIS parametersinput C_PARENTHESIS generate_gosub add_c_parenthesis
                     | add_to_stack'''
  # ''' functionorlist : add_list_variable O_S_BRACKET expression C_S_BRACKET add_list_index_to_stack
  #                    | check_function_exists O_PARENTHESIS parametersinput C_PARENTHESIS generate_gosub
  #                    | add_to_stack'''

# Llamar a función semántica para agregar la variable a la lista de listas
def p_add_list_variable(p):
  ''' add_list_variable : '''
  add_list_variable(p[-1])

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

# Las siguientes cuatro reglas son para agregar constantes al diccionario de constantes
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

# Regla para ciclo de funciones.
def p_functionloops(p):
  ''' functionloops : functionwhileloop
                   | functiontimesloop'''

# Regla para while
def p_whileloop(p):
  ''' whileloop : WHILE start_while O_PARENTHESIS expression C_PARENTHESIS condition_while block end_while'''

# Regla para el ciclo de while en una función
def p_functionwhileloop(p):
  ''' functionwhileloop : WHILE start_while O_PARENTHESIS expression C_PARENTHESIS condition_while functionblock end_while'''

# Llamar a función semántica para crear cuádruplo de inicio de while
def p_start_while(p):
  '''start_while :'''
  generate_while_start_quadruples()

# Llamar a función semántica para crear cuádruplo de condición de while
def p_condition_while(p):
  '''condition_while :'''
  generate_while_condition_quadruples()

# Llamar a función semántica para crear cuádruplo de termino de while
def p_end_while(p):
  '''end_while :'''
  generate_while_end_quadruples()

# Regla para times
def p_timesloop(p):
  ''' timesloop : TIMES O_PARENTHESIS expression C_PARENTHESIS start_times block end_times'''

# Regla para times
def p_functiontimesloop(p):
  ''' functiontimesloop : TIMES O_PARENTHESIS expression C_PARENTHESIS start_times functionblock end_times'''

# Llamar a función semántica para crear cuádruplo de inicio de ciclo times
def p_start_times(p):
  '''start_times :'''
  generate_times_start_quadruples()

# Llamar a función semántica para crear cuádruplo de terminación de ciclo times
def p_end_times(p):
  '''end_times :'''
  generate_times_end_quadruples()

# Regla de llamada de función
def p_functioncall(p):
  ''' functioncall : ID add_o_parenthesis check_function_exists O_PARENTHESIS parametersinput C_PARENTHESIS SEMICOLON generate_gosub add_c_parenthesis'''
  if var_options['scope'] == 'function':
    last_return(False)

# Llamar a función semántica para verificar si una función ya existe
def p_check_function_exists(p):
  ''' check_function_exists : '''
  check_function_exists(p[-2])
  generate_era(p[-2])

# Llamar a función semántica para crear cuádruplo de ir a función
def p_generate_gosub(p):
  ''' generate_gosub : '''
  generate_gosub()

# Regla para parametros de la función en input
def p_parametersinput(p):
  ''' parametersinput : expression push_type_to_function_options generate_parameter_quadruple parametersinputloop check_params_order
                      |'''

# Regla para ciclo de ingresar parametros a una función en input
def p_parametersinputloop(p):
  ''' parametersinputloop : COMMA expression push_type_to_function_options generate_parameter_quadruple parametersinputloop
                         |'''
# Llamar a función semántica para agregar el tipo de función a stack
def p_push_type_to_function_options(p):
  ''' push_type_to_function_options : '''
  push_type_to_function_options()

# Llamar a función semántica para verificiar orden de parametros en la llamada de una función con la función
def p_check_params_order(p):
  ''' check_params_order : '''
  check_params_order()

# # Llamar a función semántica para crear cuádruplo de parametros
def p_generate_parameter_quadruple(p):
  ''' generate_parameter_quadruple : '''
  generate_parameter_quadruple()

# Regla para parametros de una función
def p_parameters(p):
  ''' parameters : parameterinit parametersloop
                 |'''

# Regla de paramtros de uan función, ya agrega variables al diccionario de variables
def p_parameterinit(p):
  ''' parameterinit : parametertype ID '''
  var_options['id'] = p[2]
  if var_exists(var_options['id'], var_options['scope']):
    print("The variable ", var_options['id'], "has been used before.")
    exit(0)
  else:
    add_var_to_dict(var_options['id'], var_options['type'], var_options['list'], var_options['size'], var_options['scope'])
    funct_options['params'].append([var_options['id'], types[var_options['type']], var_dict['function'][var_options['id']]['address']])

# Regal para el ciclio de ingresar más parametros a uan función
def p_parametersloop(p):
  ''' parametersloop : COMMA parameterinit parametersloop
                     |'''

# Función de error del parser
def p_error(p):
    if type(p).__name__ == 'NoneType':
      print('Syntax error')
      exit(0)
    else:
      print('Syntax error in ', p.value, ' at line ', p.lineno)
      p.lineno = 0
      exit(0)

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
  f = open('test/fibo_ciclico.txt', 'r')
  data = f.read()
  f.close()
  if parser.parse(data) == 'Valid':
    print('VALID!')
    print_quadruplets()
    # print_funct_dict()
    # print_var_dict()
    #print_global_dict()
    solve()

  exit(0);

# Función que compila
if __name__ == '__main__':
  # Revisa si el archivo se dio como input
  if (len(sys.argv) > 2):
    data = sys.argv[1]
    options = sys.argv[2]
    if options == 'solve':
      if parser.parse(data) == 'Valid':
        # print('VALID!')
        # print_quadruplets()
        # print_funct_dict()
        # print_var_dict()
        #print_global_dict()
        solve()
    elif options == 'syntax_check':
      if parser.parse(data) == 'Valid':
        print('This code is valid!')
    elif options == 'print_quadruplets':
      if parser.parse(data) == 'Valid':
        print_quadruplets()
  else:
    print('Param missing')