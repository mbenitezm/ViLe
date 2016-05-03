# -*- coding: utf-8 -*-
# Semántica del compilador
import pprint
from collections import deque
pp = pprint.PrettyPrinter()

###### Initialize structures ###################################################

# Estructura de memoria necesaria para memoria global
global_dict = {'global_memory_needed' : None }

# Diccionario de funciones
funct_dict = {}

# Traducción de tipos a enteros.
types = {
  'int' : 1,
  'float' : 2,
  'string' : 3,
  'bool' : 4 ,
  'void' : 5,
  'error': -1
}

# Traducción de enteros a tipos
types_translations = {
  1 : 'int',
  2 : 'float',
  3 : 'string',
  4 : 'bool',
  5 : 'void',
  -1 : 'error'
}

# Diccionario de variables
var_dict = {
    'global' : {
    },
    'main' : {
     },
    'function' : {
    },
    'constants' : {
    },
    'inverse_constants' : {
    }
}

# Diccionario de opciones de variables
var_options = {
  'id' : None,
  'scope' : 'function',
  'type' : None,
  'list' : False,
  'size' : None
}

# Diccionario de opciones de funciones
funct_options = {
  'id' : None,
  'start': None,
  'type' : None,
  'params' : [],
  'params_order' : '',
  'memory_needed' : {}
}

# Stack de funciones
current_function_check = []

# Valores de la función actual
current_function = {
  'id' : None,
  'type' : None,
  'return' : False
}

current_list = []

#Cuádruplos
quadruplets = deque([])

# Stacks necesarios para generación de cuádruplos
operand_stack = []
operator_stack = []
types_stack = []
jumps_stack = []
times_temp_stack = []

# String con el orden de parámetros
function_params_order = ''

#Memoria virtual
# Memory segment int float  bool  string
main_segment = [0, 2500, 5000, 7500]
function_segment = [10000, 12500, 15000, 17500]
temp_segment = [20000, 22500, 25000, 27500]
const_segment = [30000, 32500, 35000, 37500]
global_segment = [40000, 42500, 45000, 47500]
fun_temp_segment = [50000, 52500, 55000, 57500]

# Esta función maneja los contadores de la memoria virtual de la sección main. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable del main truena
def add_main_memory(var_type):
    if var_type == 'int':
      if main_segment[0] > 2499:
        print('Memory overflow')
        exit(-1)
      else: 
        main_segment[0] += 1
    elif var_type == 'float':
      if main_segment[1] > 4999:
        print('Memory overflow')
        exit(-1)
      else:
        main_segment[1] += 1
    elif var_type == 'bool':
      if main_segment[2] > 7499:
        print('Memory overflow')
        exit(-1)
      else:
        main_segment[2] += 1
    elif var_type == 'string':
      if main_segment[3] > 9999:
        print('Memory overflow')
        exit(-1)
      else:
        main_segment[3] += 1

# Esta función maneja los contadores de la memoria virtual de la sección función. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable de la función truena
def add_function_memory(var_type):
  if var_type == 'int':
    if function_segment[0] > 12499:
      print('Memory overflow')
      exit(-1)
    else: 
      function_segment[0] += 1
  elif var_type == 'float':
    if function_segment[1] > 14999:
      print('Memory overflow')
      exit(-1)
    else:
      function_segment[1] += 1
  elif var_type == 'bool':
    if functionl_segment[2] > 17499:
      print('Memory overflow')
      exit(-1)
    else:
      function_segment[2] += 1
  elif var_type == 'string':
    if function_segment[3] > 19999:
      print('Memory overflow')
      exit(-1)
    else:
      function_segment[3] += 1

# Esta función maneja los contadores de la memoria virtual de la sección temporales de main. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable de temporales de mainruena
def add_temp_memory(var_type):
  if var_type == 1:
    if temp_segment[0] > 22499:
      print('Memory overflow')
      exit(-1)
    else: 
      temp_segment[0] += 1
  elif var_type == 2:
    if temp_segment[1] > 24999:
      print('Memory overflow')
      exit(-1)
    else:
      temp_segment[1] += 1
  elif var_type == 3:
    if temp_segment[2] > 27499:
      print('Memory overflow')
      exit(-1)
    else:
      temp_segment[2] += 1
  elif var_type == 4:
    if temp_segment[3] > 29999:
      print('Memory overflow')
      exit(-1)
    else:
      temp_segment[3] += 1

# Esta función maneja los contadores de la memoria virtual de la sección temporales de función. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable de las temporales de función truena
def add_fun_temp_memory(var_type):
  if var_type == 1:
    if fun_temp_segment[0] > 52499:
      print('Memory overflow')
      exit(-1)
    else: 
      fun_temp_segment[0] += 1
  elif var_type == 2:
    if fun_temp_segment[1] > 54999:
      print('Memory overflow')
      exit(-1)
    else:
      fun_temp_segment[1] += 1
  elif var_type == 3:
    if fun_temp_segment[2] > 57499:
      print('Memory overflow')
      exit(-1)
    else:
      fun_temp_segment[2] += 1
  elif var_type == 4:
    if fun_temp_segment[3] > 59999:
      print('Memory overflow')
      exit(-1)
    else:
      fun_temp_segment[3] += 1

# Esta función maneja los contadores de la memoria virtual de constantes. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable de las constantes truena
def add_constant_memory(var_type):
  if var_type == 'int':
    if const_segment[0] > 32499:
      print('Memory overflow')
      exit(-1)
    else: 
      const_segment[0] += 1
  elif var_type == 'float':
    if const_segment[1] > 34999:
      print('Memory overflow')
      exit(-1)
    else:
      const_segment[1] += 1
  elif var_type == 'bool':
    if const_segment[2] > 37499:
      print('Memory overflow')
      exit(-1)
    else:
      const_segment[2] += 1
  elif var_type == 'string':
    if const_segment[3] > 39999:
      print('Memory overflow')
      exit(-1)
    else:
      const_segment[3] += 1

# Esta función maneja los contadores de la memoria virtual de la sección global. 
# Cuando se asigna una variable, se suma a su tipo correspondiente uno.
# También maneja los overflows de un lenguaje, es decir, cuando se acaba la memoria
# disponible para alguan variable del global truena
def add_global_memory(var_type):
  if var_type == 'int':
    if global_segment[0] > 42499:
      print('Memory overflow')
      exit(-1)
    else: 
      global_segment[0] += 1
  elif var_type == 'float':
    if global_segment[1] > 44999:
      print('Memory overflow')
      exit(-1)
    else:
      global_segment[1] += 1
  elif var_type == 'bool':
    if global_segment[2] > 47499:
      print('Memory overflow')
      exit(-1)
    else:
      global_segment[2] += 1
  elif var_type == 'string':
    if global_segment[3] > 49999:
      print('Memory overflow')
      exit(-1)
    else:
      global_segment[3] += 1

# Esta función resetea la memoria virtual de las funciones cada que esta finalice
# para que otras funciones puedan tomar las direcciones.
def release_fun_temp_memory():
  fun_temp_segment[0] = 50000
  fun_temp_segment[1] = 52500
  fun_temp_segment[2] = 55000
  fun_temp_segment[3] = 57500
  function_segment[0] = 10000
  function_segment[1] = 12500
  function_segment[2] = 15000
  function_segment[3] = 17500

########################Quadruple Generation####################################

# Genera el cuádruplo de goto al main
def generate_main_goto():
  global quadruplets
  quadruple = ["GOTO", "", "", ""]
  quadruplets.append(quadruple)

# Prende bandera de que el main se prendió
def start_main():
  var_options['scope'] = 'main'
  funct_options['start'] = get_current_quadruple()

# Rellena el salto del cuádruplo goto del main.
def fill_main_goto():
  global quadruplets
  quadruplets[0][3] = len(quadruplets)

# Genera el cuádruplo de de operaciones
def generate_operations_quadruples(scope, memory_pointer = None):
  type2 = types_stack.pop() # Se saca el tipo 2 de del stack de tipos
  type1 = types_stack.pop() # Se saca el tipo 1 del stack de tipos
  operator1 = operator_stack.pop() # Se saca el operador del stack de operadores
  result_type = semantic_dict[type1][type2][operator1]
  if result_type < 1: # Se hace la verificación de la operación que se quiere realizar es valida
    print types_translations[type1], " and ", types_translations[type2], " are not a valid type combination for ", operator1 
    exit(0)
  else:
    operand2 = operand_stack.pop() # Se saca el operando 2
    operand1 = operand_stack.pop() # Se saca el operando 1
    if scope == 'main':
      result = assign_address('temps', result_type) # El resultado se asigna a memoria virtual de temporal si es mail
    else:
      result = assign_address('function_temps', result_type) # Si es una función se asigna a la memoria virtual de temporales de funciones
    quadruple = [operator1, operand1, type1, operand2, type2, result, result_type] # Se genera el cuádruplo
    if memory_pointer != None: # Se verifia si es un arreglo, si si lo es se mete la dirección indirecta a los operandos.
      operand_stack.append(-result)
      types_stack.append(memory_pointer)
    else:
      operand_stack.append(result)
      types_stack.append(result_type)
    quadruplets.append(quadruple)
    # print quadruple

# Genera el cuádruplo de asignación
def generate_equals_quadruples():
  type2 = types_stack.pop()
  type1 = types_stack.pop()
  operator1 = operator_stack.pop()
  result_type = semantic_dict[type1][type2][operator1]
  if result_type < 1:
    print types_translations[type1], " and ", types_translations[type2], " are not a valid type combination for ", operator1
    exit(0)
  else:
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    quadruple = [operator1, operand2, type2, '',  operand1, type1]
    quadruplets.append(quadruple)
    # print quadruple

# Genera el cuádruplo de condición del if
def generate_condition_if_quadruples():
  global quadruplets
  # Saca el tipo del stakc de tipo, si no es una booleana marca error
  type1 = types_stack.pop()
  if type1 != 4:
    print type1, " is not a valid operation in a condition."
  else:
    # El resultado de esta condición esta en la pila de operandos
    result = operand_stack.pop()
    # Se genera el cuádruplo GOTOF
    quadruple = ["GOTOF", result, type1, "", ""]
    quadruplets.append(quadruple)
    jumps_stack.append(len(quadruplets) - 1)
    # print quadruple

# Genera el cuádruplo de de condición del else
def generate_condition_else_quadruples():
  global quadruplets
  # Se genera el cuádruplo GOTO
  quadruple = ["GOTO", "", "", ""]
  quadruplets.append(quadruple)
  # Se saca el salto de donde empezó el if de la pila de saltos
  jump = jumps_stack.pop()
  # Se rellena el cuádruplo de gotof con el cuádruplo actual
  quadruplets[jump][3] = len(quadruplets)
  # Se agrega el número de cuádruplo al stack de saltos
  jumps_stack.append(len(quadruplets) - 1)
  # print quadruple

# Genera el cuádruplo de terminación del if
def generate_condition_end_quadruples():
  # Se rellena el cuádurplo de Goto con el cuádruplo actual
  global quadruplets
  jump = jumps_stack.pop()
  quadruplets[jump][3] = len(quadruplets)

# Genera el cuádruplo de inicio del while
def generate_while_start_quadruples():
  global quadruplets
  quadruple = ["WHILE", "", "", ""]
  quadruplets.append(quadruple)
  jumps_stack.append(len(quadruplets))

# Genera el cuádruplo de condición del while
def generate_while_condition_quadruples():
  global quadruplets
  type1 = types_stack.pop()
  if type1 != types['bool']:
    print type1, " is not a valid operation in a condition."
  else:
    result = operand_stack.pop()
    quadruple = ["GOTOF", result, type1, "", ""]
    quadruplets.append(quadruple)
    jumps_stack.append(len(quadruplets) - 1)
    # print quadruple 

# Genera el cuádruplo de finalización del while
def generate_while_end_quadruples():
  global quadruplets
  jump_false = jumps_stack.pop()
  jump_return = jumps_stack.pop()
  quadruplets.append(["GOTO", "", "", jump_return])
  quadruplets[jump_false][3] = len(quadruplets)
  quadruple = ["ENDWHILE", "", "", ""]
  quadruplets.append(quadruple)

# Genera el cuádruplo de inicio del ciclo times
def generate_times_start_quadruples():
  global quadruplets
  int_type = types_stack.pop()
  if int_type != types['int']:
    print "Times loop just accepts integer numbers"
    exit(0)
  times_temp_aux = temp_segment[0]
  temp_segment[0] += 1
  times_temp_stack.append(times_temp_aux)
  int_value = operand_stack.pop()
  types_stack.append(int_type)
  types_stack.append(int_type)
  operand_stack.append(times_temp_aux)
  operand_stack.append(int_value)
  operator_stack.append('=')
  generate_equals_quadruples()
  operand_stack.append(times_temp_aux)
  types_stack.append(int_type)
  add_constant_to_dict(0, 'int')
  operator_stack.append('>')
  jumps_stack.append(len(quadruplets))
  generate_operations_quadruples(var_options['scope'])
  bool_type = types_stack.pop()
  result = operand_stack.pop()
  quadruple = ["GOTOF", result, bool_type, "", ""]
  quadruplets.append(quadruple)
  # print quadruple

# Genera el cuádruplo de finalización del times.
def generate_times_end_quadruples():
  global quadruplets
  jump_return = jumps_stack.pop()
  times_temp_aux = times_temp_stack.pop()
  operand_stack.append(times_temp_aux)
  types_stack.append(types['int'])
  operand_stack.append(times_temp_aux)
  types_stack.append(types['int'])
  add_constant_to_dict(1, 'int')
  operator_stack.append('-')
  generate_operations_quadruples(var_options['scope'])
  operator_stack.append('=')
  generate_equals_quadruples()
  quadruplets.append(["GOTO", "", "", jump_return])
  quadruplets[jump_return + 1][3] = len(quadruplets)

# Genera el cuádruplo de print
def generate_print_quadruples():
  temp_type = types_stack.pop()
  print_operator = operator_stack.pop()
  print_operand = operand_stack.pop()
  quadruple = [print_operator, '', '',  print_operand, temp_type]
  quadruplets.append(quadruple)
  # print quadruple

# Agrega al stack de operandos y operadores el id de la variable de lista
def semantics_add_to_stack(id):
  if id in var_dict['function']:
    if var_dict['function'][id]['list']:
      print('You must give an index if you are trying to access a list')
      exit(0)
    else:
      operand_stack.append(var_dict['function'][id]['address'])
      types_stack.append(var_dict['function'][id]['type'])
  elif id in var_dict['main']:
    if var_dict['main'][id]['list']:
      print('You must give an index if you are trying to access a list')
      exit(0)
    else:
      operand_stack.append(var_dict['main'][id]['address'])
      types_stack.append(var_dict['main'][id]['type'])
  else:
    print id, " doesn't exists"
    exit(0)

# Genera el cuádruplo para asignación de parametros de llamada con los de la función
def generate_parameter_quadruple():
  global quadruplets
  type1 = types_stack.pop()
  result = operand_stack.pop()
  function_check = current_function_check[len(current_function_check) - 1]
  if function_check['current_param'] > (len(funct_dict[function_check['id']]['params']) - 1):
    print('The params in ' + function_check['id'] + ' are wrong')
    exit(0)
  current_param = funct_dict[function_check['id']]['params'][function_check['current_param']][2]
  current_function_check[len(current_function_check) - 1]['current_param'] = current_function_check[len(current_function_check) - 1]['current_param'] + 1
  quadruple = ["PARAM", result, type1, "", current_param, type1]
  quadruplets.append(quadruple)
  # print quadruple

# Genera el cuádruplo de ERA, para hacer inicializar memorias
def generate_era(function_id):
  global quadruplets
  quadruple = ["ERA", "", "", function_id]
  quadruplets.append(quadruple)
  # print quadruple
  if funct_dict[function_id]['type'] != types['void']:
    if var_options['scope'] == 'main':
      result = assign_address('temps', var_dict['global'][function_id]['type'])
    else:
      result = assign_address('function_temps', var_dict['global'][function_id]['type'])
    types_stack.append(var_dict['global'][function_id]['type'])
    operand_stack.append(result)
    types_stack.append(var_dict['global'][function_id]['type'])
    operand_stack.append(result)

# Genera el cuádruplo de ir a subrutina
def generate_gosub():
  global quadruplets
  function_check = current_function_check[len(current_function_check) - 1]
  quadruple = ["GOSUB", "", "", function_check['id']]
  quadruplets.append(quadruple)
  # print quadruple
  if funct_dict[function_check['id']]['type'] != 5:
    types_stack.append(var_dict['global'][function_check['id']]['type'])
    operand_stack.append(var_dict['global'][function_check['id']]['address'])
    operator_stack.append('=')
    generate_equals_quadruples()
  current_function_check.pop()

# Genera el cuádruplo de finalización de función
def create_function_end_quadruple():
  global quadruplets
  quadruple = ["ENDFUNCTION", "", "", ""]
  quadruplets.append(quadruple)
  # print quadruple

# Genera el cuádruplo de retorno de función
def create_function_return_quadruple():
  global quadruplets
  quadruple = ["RETURN", "", "", ""]
  quadruplets.append(quadruple)
  # print quadruple

# Regresa el cuádruplo actual
def get_current_quadruple():
  global quadruplets
  return len(quadruplets)

# Genera el cuádruplo de finalización de programa
def generate_end_all_quadruple():
  global quadruplets
  quadruple = ["ENDALL"]
  quadruplets.append(quadruple)
  # print quadruple

# Genera el cuádruplo de asignación a una lista
def generate_list_assignation_quadruple():
  type2 = types_stack.pop()
  operand2 = operand_stack.pop()
  type1 = types[var_options['type']]
  address = assign_address(var_options['scope'], var_options['type'])
  operand1 = address
  types_stack.append(type1)
  types_stack.append(type2)
  operand_stack.append(operand1)
  operand_stack.append(operand2)
  operator_stack.append('=')
  generate_equals_quadruples()

# Genera el cuádruplo de verificación de índices de una lista
def generate_ver_quadruple(var_id):
  global quadruplets
  if var_id in var_dict[var_options['scope']]:
    if var_dict[var_options['scope']][var_id]['list']:
      operand = operand_stack[len(operand_stack) -1]
      operand_type = types_stack[len(types_stack) -1]
      if operand_type != types['int']:
        print("Error in "+ var_id + ": To access a list element, you must provide an integer")
        exit(0)
      if not('0' in var_dict['constants']):
        add_constant_to_dict_aux('0', 'int')
      if not(str(var_dict[var_options['scope']][var_id]['size'] - 1 ) in var_dict['constants']):
        add_constant_to_dict_aux(str(var_dict[var_options['scope']][var_id]['size'] - 1), 'int')
      quadruple = ["VER", operand, var_dict['constants']['0']['address'], var_dict['constants'][str(var_dict[var_options['scope']][var_id]['size'] - 1)]['address']]
      quadruplets.append(quadruple)
      # print quadruple
    else:
      print("Error in "+ var_id + ": This variable is not a list")
      exit(0)
  else:
    print("Error in "+ var_id + ": This list doesn't exists")
    exit(0)

################################################################################
# Impresiones para debugging
def print_var_dict():
  print "\nVAR DICT"
  pp.pprint(var_dict)

def print_funct_dict():
  print "\nFUNCT DICT"
  pp.pprint(funct_dict)

def print_quadruplets():
  print "\nQuadruplets"
  global quadruplets
  for quadruplet in quadruplets:
    pp.pprint(quadruplet)

def print_global_dict():
  print "\GLOBAL DICT"
  pp.pprint(global_dict)

# Cubo semántico
def semantic_dict_constr():
  return { 
          types['int'] : { 
            types['int'] : op_constr('int', 'int', 'int', 'int', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'int', 'bool', 'int'),
            types['float'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'error', 'bool', 'float'),
            types['string'] : op_error(),
            types['bool'] : op_error()
          },
          types['float'] : { 
            types['int'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'float', 'bool', 'float'),
            types['float'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'float', 'bool', 'float'),
            types['string'] : op_error(),
            types['bool'] : op_error()
          },
         types['string'] : { 
            types['int'] : op_error(),
            types['float'] : op_error(),
            types['string'] : op_constr('string', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'error', 'error', 'string', 'bool', 'error'),
            types['bool'] : op_error()
          },
          types['bool'] : { 
            types['int'] : op_error(),
            types['float'] : op_error(),
            types['string'] : op_error(),
            types['bool'] : op_constr('error', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'bool', 'bool', 'bool', 'bool', 'error')
          }
         }

# Construcción de cubo semántico
def op_constr(plus, minus, mult, div, greater_than, greater_eq_than, less_than, less_eq_than, equals, and_o, or_o, equal, not_equal, mod):
  return { '+' : types[plus], '-' : types[minus], '*' : types[mult], '/' : types[div], '>' : types[greater_than], '>=' : types[greater_eq_than],
    '<' : types[less_than], '<=' : types[less_eq_than], '==' : types[equals], 'and' : types[and_o], 'or' : types[or_o], '=' : types[equal],
    '!=' : types[not_equal], '%' : types[mod]}

# Construcción de cubo semántico
def op_error():
  return { '+' : types['error'], '-' : types['error'], '*' : types['error'], '/' : types['error'], '>' : types['error'], '>=' : types['error'],
    '<' : types['error'], '<=' : types['error'], '==' : types['error'], 'and' : types['error'], 'or' : types['error'], '=' : types['error'],
    '!=' : types['error'], '%' : types['error']}

semantic_dict = semantic_dict_constr()

# Agrega una variable al diccionario de variables
def add_var_to_dict(var_id, var_type, var_list, var_size, scope):
  address = assign_address(scope, var_type)

  var_dict[scope][var_id] = {
    'type': types[var_type],
    'address' : address,
    'list' : var_list,
    'size' : var_size
  }
  clean_var_options(scope)
  # print_var_dict()

# Agrega una lista al diccionario de variables
def add_list_to_dict(var_id, var_type, var_list, var_size, scope):
  list_options = current_list[len(current_list) - 1]
  address = list_options['start_address']
  var_dict[scope][var_id] = {
    'type': types[var_type],
    'address' : address,
    'list' : var_list,
    'size' : var_size
  }
  clean_var_options(scope)
  current_list.pop()
  # print_var_dict()

# Resetea las banderas de las variables
def clean_var_options(scope):
  var_options = {
    'id' : None,
    'scope' : scope,
    'type' : None,
    'list' : False,
    'size' : None
  }

# Esta función regresa la dirección de memoria virtual correspondiente que 
# se le dará a una variable, dependiendo su scope y su tipo.
def get_current_memory(scope, var_type):
  if scope == 'main':
    if var_type == 'int':
      address = main_segment[0]
    elif var_type == 'float':
      address = main_segment[1]
    elif var_type == 'bool':
      address = main_segment[2]
    elif var_type == 'string':
      address = main_segment[3]
  elif scope == 'function':
    if var_type == 'int':
      address = function_segment[0]
    elif var_type == 'float':
      address = function_segment[1]
    elif var_type == 'bool':
      address = function_segment[2]
    elif var_type == 'string':
      address = function_segment[3]
  elif scope == 'constants':
    if var_type == 'int':
      address = const_segment[0]
    elif var_type == 'float':
      address = const_segment[1]
    elif var_type == 'bool':
      address = const_segment[2]
    elif var_type == 'string':
      address = const_segment[3]
  elif scope == 'temps':
    if var_type == 1:
      address = temp_segment[0]
    elif var_type == 2:
      address = temp_segment[1]
    elif var_type == 4:
      address = temp_segment[2]
    elif var_type == 3:
      address = temp_segment[3]
  elif scope == 'function_temps':
    if var_type == 1:
      address = fun_temp_segment[0]
    elif var_type == 2:
      address = fun_temp_segment[1]
    elif var_type == 4:
      address = fun_temp_segment[2]
    elif var_type == 3:
      address = fun_temp_segment[3]
  elif scope == 'global':
    if var_type == 'int':
      address = global_segment[0]
    elif var_type == 'float':
      address = global_segment[1]
    elif var_type == 'bool':
      address = global_segment[2]
    elif var_type == 'string':
      address = global_segment[3]
  return address

# Esta función asigna el valor a la variable con la dirección que fue obtenida
# por la función anterior.
def assign_address(scope, var_type):
  if scope == 'main':
    if var_type == 'int':
      address = main_segment[0]
    elif var_type == 'float':
      address = main_segment[1]
    elif var_type == 'bool':
      address = main_segment[2]
    elif var_type == 'string':
      address = main_segment[3]
    add_main_memory(var_type)
  elif scope == 'function':
    if var_type == 'int':
      address = function_segment[0]
    elif var_type == 'float':
      address = function_segment[1]
    elif var_type == 'bool':
      address = function_segment[2]
    elif var_type == 'string':
      address = function_segment[3]
    add_function_memory(var_type)
  elif scope == 'constants':
    if var_type == 'int':
      address = const_segment[0]
    elif var_type == 'float':
      address = const_segment[1]
    elif var_type == 'bool':
      address = const_segment[2]
    elif var_type == 'string':
      address = const_segment[3]
    add_constant_memory(var_type)
  elif scope == 'temps':
    if var_type == 1:
      address = temp_segment[0]
    elif var_type == 2:
      address = temp_segment[1]
    elif var_type == 4:
      address = temp_segment[2]
    elif var_type == 3:
      address = temp_segment[3]
    add_temp_memory(var_type)
  elif scope == 'function_temps':
    if var_type == 1:
      address = fun_temp_segment[0]
    elif var_type == 2:
      address = fun_temp_segment[1]
    elif var_type == 4:
      address = fun_temp_segment[2]
    elif var_type == 3:
      address = fun_temp_segment[3]
    add_fun_temp_memory(var_type)
  elif scope == 'global':
    if var_type == 'int':
      address = global_segment[0]
    elif var_type == 'float':
      address = global_segment[1]
    elif var_type == 'bool':
      address = global_segment[2]
    elif var_type == 'string':
      address = global_segment[3]
    add_global_memory(var_type)
  return address

# Agregar constante a diccionario
def add_constant_to_dict_aux(constant, type):
  address = assign_address('constants', type)
  var_dict['constants'][constant] = {
    'address' : address,
    'type' : types[type]
  }
  if(types[type] == 1):
    constant = int(constant)
  elif(types[type] == 2):
    constant = float(constant)
  elif(types[type] == 4):
    if constant == "true":
      constant = True;
    elif constant == "false":
      constant = False;
  var_dict['inverse_constants'][address] = {
    'value' : constant, 
    'type' : types[type]
  }

# Agrear función a diccionario de funciones
def add_funct_to_dict(funct_id, funct_type, funct_params, funct_params_order, funct_start, funct_memory_needed):
  funct_dict[funct_id] = {
    'start' : funct_start,
    'type' : types[funct_type],
    'params' : funct_params,
    'params_order' : funct_params_order,
    'memory_needed' : funct_memory_needed
  }

# Agregar constante a diccionario
def add_constant_to_dict(constant, type):
  if not(constant in var_dict['constants']):
    add_constant_to_dict_aux(constant, type)
    operand_stack.append(var_dict['constants'][constant]['address'])
    types_stack.append(var_dict['constants'][constant]['type'])
  else:
    operand_stack.append(var_dict['constants'][constant]['address'])
    types_stack.append(var_dict['constants'][constant]['type'])

# Revisa si una variable ya fue declara en la función actual
def var_exists(var_id, scope):
  if var_id in var_dict[scope]:
    return True
  else:
    return False

# Elimina todas las variables de funciones del diccionario de variables
def clear_var_dict():
  var_dict['function'].clear()

# Resetea las banderas de las variables
def reset_options():
  var_options = {
    'id' : None,
    'scope' : 'main',
    'type' : None,
  }

# Regresa la memoria necesaria que necesitara el main y agrega el main al diccionario de funciones
def add_main_to_dict():
  memory_needed = variable_counts(main_segment[0], main_segment[1] - 2500, main_segment[2] - 5000, main_segment[3] - 7500,
                                  temp_segment[0] - 20000, temp_segment[1] - 22500, temp_segment[2] - 25000, temp_segment[3] - 27500)
  add_funct_to_dict('main', 'void', {}, '', funct_options['start'], memory_needed)

# Resetea las banderas del diccionario de funciones
def clean_funct_options():
  funct_options = {
    'id' : None,
    'type' : None,
    'params' : [],
    'params_order' : ''
  }

# Contador de variables para asignación de memoria real.
def variable_counts(int_q, float_q, bool_q, string_q, temp_int_q, temp_float_q, temp_string_q, temp_bool_q):
  return { 'int' : int_q, 'float' : float_q, 'string' : string_q, 'bool' : bool_q, 
           'temp_int' : temp_int_q, 'temp_float' : temp_float_q, 'temp_string' : temp_string_q, 'temp_bool' : temp_bool_q,}

######################### FUNCTIONS METHODS ####################################

# Verifica el tipo de función esperado de una función con el real.
def check_function_return():
  return_type = types_stack.pop()
  if return_type != var_dict['global'][current_function['id']]['type']:
    print('Return type of the function ' + current_function['id'] + ' is not correct')
    print('It returns ' + types_translations[return_type] + ' and it should be ' + types_translations[var_dict['global'][current_function['id']]['type']])
    exit(0)
  types_stack.append(return_type)
  current_function['return'] = True
  last_return(True)

# Valida que exista un return cuándo la función no es vacía
def validate_function_return():
  if not (current_function['return']):
    print('Function must have at least one return')
    exit(0)
  if not (current_function['last_return']):
    print("There is a case when the function doesn't end with a return")
    exit(0)

# Revisa si la función existe cuando se llama
def check_function_exists(function_name):
  if not(function_name in funct_dict):
    print('The function "' + function_name + '" is not a function')
    exit(0)
  else:
    current_function_check.append({'id' : function_name, 'params_order' : '', 'current_param' : 0})

# Agrega el tipo de función a las opciones de la función
def push_type_to_function_options():
  current_type = types_stack[len(types_stack) - 1]
  current_function_check[len(current_function_check) - 1]['params_order'] = current_function_check[len(current_function_check) - 1]['params_order'] + str(current_type)

# Compara y verifica que los parametros de la llamada de un función correspondan con esta.
def check_params_order():
  function_check = current_function_check[len(current_function_check) - 1]
  if function_check['params_order'] != funct_dict[function_check['id']]['params_order']:
    print('The params in ' + function_check['id'] + ' are wrong')
    exit(0)

# Agrega la función global como variable al diccionario de variables para la asignación al retorno
def add_function_to_global_variables(function_id, function_type):
  current_function['id'] = function_id
  current_function['type'] = function_type
  add_var_to_dict(function_id, function_type, False, None , 'global')

# Agrega la variable de la función a los stacks
def add_function_var_to_stack():
  types_stack.append(var_dict['global'][current_function['id']]['type'])
  operand_stack.append(var_dict['global'][current_function['id']]['address'])
  operator_stack.append('=')

# Regresa la memoria necesaria para la memoria global
def get_global_memory_needed():
  global_dict['global_memory_needed'] = variable_counts(global_segment[0] - 40000, global_segment[1] - 42500, 
                                                       global_segment[2] - 45000, global_segment[3] - 47500,
                                                       0, 0, 0, 0)

# Regeresa la memoria necesaria para una función
def get_memory_needed_for_function():
  return variable_counts(function_segment[0] - 10000, function_segment[1] - 12500, function_segment[2] - 15000, function_segment[3] - 17500,
                         fun_temp_segment[0] - 50000, fun_temp_segment[1] - 52500, fun_temp_segment[2] - 55000, fun_temp_segment[3] - 57500)

# Actualiza la memoria necesaria para la memoria real de las funciones
def update_funct_memory(function_id, function_memory_needed):
  funct_dict[function_id]['memory_needed'] = function_memory_needed

# agrega el ultimo retorno de la función
def last_return(value):
  current_function['last_return'] = value

############################# LISTS METHODS ####################################

# Agrega a la lista de listas el id y su dirección de inicio
def add_list_variable(var_id):
  current_list.append({'id' : var_id, 'start_address' : None })

# Agrega el indice de la lista al stack.
def add_list_index_to_stack():
  list_options = current_list[len(current_list) - 1]
  generate_ver_quadruple(list_options['id'])
  generate_list_index(list_options['id'])
  current_list.pop()

# Genera el indice de la lista.
def generate_list_index(var_id):
  operator_stack.append('+')
  if not(str(var_dict[var_options['scope']][var_id]['address']) in var_dict['constants']):
    add_constant_to_dict_aux(str(var_dict[var_options['scope']][var_id]['address']), 'int')
  operand_stack.append(var_dict['constants'][str(var_dict[var_options['scope']][var_id]['address'])]['address'])
  types_stack.append(types['int'])
  generate_operations_quadruples(var_options['scope'], var_dict[var_options['scope']][var_id]['type'])