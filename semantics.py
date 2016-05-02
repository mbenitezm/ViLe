  # -*- coding: utf-8 -*-
import pprint
from collections import deque
pp = pprint.PrettyPrinter()

###### Initialize structures ###################################################

global_dict = {'global_memory_needed' : None }

funct_dict = {}

types = {
  'int' : 1,
  'float' : 2,
  'string' : 3,
  'bool' : 4 ,
  'void' : 5,
  'error': -1
}

types_translations = {
  1 : 'int',
  2 : 'float',
  3 : 'string',
  4 : 'bool',
  5 : 'void',
  -1 : 'error'
}

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

var_options = {
  'id' : None,
  'scope' : 'function',
  'type' : None,
  'list' : False,
  'size' : None
}

funct_options = {
  'id' : None,
  'start': None,
  'type' : None,
  'params' : [],
  'params_order' : '',
  'memory_needed' : {}
}

current_function_check = []

current_function = {
  'id' : None,
  'type' : None,
  'return' : False
}

current_list = []

quadruplets = deque([])

operand_stack = []
operator_stack = []
types_stack = []
jumps_stack = []
times_temp_stack = []

function_params_order = ''

# Memory segment int float  bool  string
main_segment = [0, 2500, 5000, 7500]
function_segment = [10000, 12500, 15000, 17500]
temp_segment = [20000, 22500, 25000, 27500]
const_segment = [30000, 32500, 35000, 37500]
global_segment = [40000, 42500, 45000, 47500]
fun_temp_segment = [50000, 52500, 55000, 57500]

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
def generate_main_goto():
  global quadruplets
  quadruple = ["GOTO", "", "", ""]
  quadruplets.append(quadruple)

def start_main():
  var_options['scope'] = 'main'
  funct_options['start'] = get_current_quadruple()

def fill_main_goto():
  global quadruplets
  quadruplets[0][3] = len(quadruplets)

def generate_operations_quadruples(scope, memory_pointer = None):
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
    if scope == 'main':
      result = assign_address('temps', result_type)
    else:
      result = assign_address('function_temps', result_type)
    quadruple = [operator1, operand1, type1, operand2, type2, result, result_type]
    if memory_pointer != None:
      operand_stack.append(-result)
      types_stack.append(memory_pointer)
    else:
      operand_stack.append(result)
      types_stack.append(result_type)
    quadruplets.append(quadruple)
    # print quadruple

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

def generate_condition_if_quadruples():
  global quadruplets
  type1 = types_stack.pop()
  if type1 != 4:
    print type1, " is not a valid operation in a condition."
  else:
    result = operand_stack.pop()
    quadruple = ["GOTOF", result, type1, "", ""]
    quadruplets.append(quadruple)
    jumps_stack.append(len(quadruplets) - 1)
    # print quadruple

def generate_condition_else_quadruples():
  global quadruplets
  quadruple = ["GOTO", "", "", ""]
  quadruplets.append(quadruple)
  jump = jumps_stack.pop()
  quadruplets[jump][3] = len(quadruplets)
  jumps_stack.append(len(quadruplets) - 1)
  # print quadruple

def generate_condition_end_quadruples():
  global quadruplets
  jump = jumps_stack.pop()
  quadruplets[jump][3] = len(quadruplets)

def generate_while_start_quadruples():
  global quadruplets
  jumps_stack.append(len(quadruplets) - 1)

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

def generate_while_end_quadruples():
  global quadruplets
  jump_false = jumps_stack.pop()
  jump_return = jumps_stack.pop()
  quadruplets.append(["GOTO", "", "", jump_return + 1])
  quadruplets[jump_false][3] = len(quadruplets)

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

def generate_print_quadruples():
  temp_type = types_stack.pop()
  print_operator = operator_stack.pop()
  print_operand = operand_stack.pop()
  quadruple = [print_operator, '', '',  print_operand, temp_type]
  quadruplets.append(quadruple)
  # print quadruple

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

def create_function_end_quadruple():
  global quadruplets
  quadruple = ["ENDFUNCTION", "", "", ""]
  quadruplets.append(quadruple)
  # print quadruple

def create_function_return_quadruple():
  global quadruplets
  quadruple = ["RETURN", "", "", ""]
  quadruplets.append(quadruple)
  # print quadruple

def get_current_quadruple():
  global quadruplets
  return len(quadruplets)

def generate_end_all_quadruple():
  global quadruplets
  quadruple = ["ENDALL"]
  quadruplets.append(quadruple)
  # print quadruple

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

def op_constr(plus, minus, mult, div, greater_than, greater_eq_than, less_than, less_eq_than, equals, and_o, or_o, equal, not_equal, mod):
  return { '+' : types[plus], '-' : types[minus], '*' : types[mult], '/' : types[div], '>' : types[greater_than], '>=' : types[greater_eq_than],
    '<' : types[less_than], '<=' : types[less_eq_than], '==' : types[equals], 'and' : types[and_o], 'or' : types[or_o], '=' : types[equal],
    '!=' : types[not_equal], '%' : types[mod]}

def op_error():
  return { '+' : types['error'], '-' : types['error'], '*' : types['error'], '/' : types['error'], '>' : types['error'], '>=' : types['error'],
    '<' : types['error'], '<=' : types['error'], '==' : types['error'], 'and' : types['error'], 'or' : types['error'], '=' : types['error'],
    '!=' : types['error'], '%' : types['error']}

semantic_dict = semantic_dict_constr()

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

def clean_var_options(scope):
  var_options = {
    'id' : None,
    'scope' : scope,
    'type' : None,
    'list' : False,
    'size' : None
  }


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

def add_funct_to_dict(funct_id, funct_type, funct_params, funct_params_order, funct_start, funct_memory_needed):
  funct_dict[funct_id] = {
    'start' : funct_start,
    'type' : types[funct_type],
    'params' : funct_params,
    'params_order' : funct_params_order,
    'memory_needed' : funct_memory_needed
  }

def add_constant_to_dict(constant, type):
  if not(constant in var_dict['constants']):
    add_constant_to_dict_aux(constant, type)
    operand_stack.append(var_dict['constants'][constant]['address'])
    types_stack.append(var_dict['constants'][constant]['type'])
  else:
    operand_stack.append(var_dict['constants'][constant]['address'])
    types_stack.append(var_dict['constants'][constant]['type'])

def var_exists(var_id, scope):
  if var_id in var_dict[scope]:
    return True
  else:
    return False

def clear_var_dict():
  var_dict['function'].clear()

def reset_options():
  var_options = {
    'id' : None,
    'scope' : 'main',
    'type' : None,
  }

def add_main_to_dict():
  memory_needed = variable_counts(main_segment[0], main_segment[1] - 2500, main_segment[2] - 5000, main_segment[3] - 7500,
                                  temp_segment[0] - 20000, temp_segment[1] - 22500, temp_segment[2] - 25000, temp_segment[3] - 27500)
  add_funct_to_dict('main', 'void', {}, '', funct_options['start'], memory_needed)

def clean_funct_options():
  funct_options = {
    'id' : None,
    'type' : None,
    'params' : [],
    'params_order' : ''
  }

def variable_counts(int_q, float_q, bool_q, string_q, temp_int_q, temp_float_q, temp_string_q, temp_bool_q):
  return { 'int' : int_q, 'float' : float_q, 'string' : string_q, 'bool' : bool_q, 
           'temp_int' : temp_int_q, 'temp_float' : temp_float_q, 'temp_string' : temp_string_q, 'temp_bool' : temp_bool_q,}

######################### FUNCTIONS METHODS ####################################

def check_function_return():
  return_type = types_stack.pop()
  if return_type != var_dict['global'][current_function['id']]['type']:
    print('Return type of the function ' + current_function['id'] + ' is not correct')
    print('It returns ' + types_translations[return_type] + ' and it should be ' + types_translations[var_dict['global'][current_function['id']]['type']])
    exit(0)
  types_stack.append(return_type)
  current_function['return'] = True
  last_return(True)

def validate_function_return():
  if not (current_function['return']):
    print('Function must have at least one return')
    exit(0)
  if not (current_function['last_return']):
    print("There is a case when the function doesn't end with a return")
    exit(0)

def check_function_exists(function_name):
  if not(function_name in funct_dict):
    print('The function "' + function_name + '" is not a function')
    exit(0)
  else:
    current_function_check.append({'id' : function_name, 'params_order' : '', 'current_param' : 0})

def push_type_to_function_options():
  current_type = types_stack[len(types_stack) - 1]
  current_function_check[len(current_function_check) - 1]['params_order'] = current_function_check[len(current_function_check) - 1]['params_order'] + str(current_type)

def check_params_order():
  function_check = current_function_check[len(current_function_check) - 1]
  if function_check['params_order'] != funct_dict[function_check['id']]['params_order']:
    print('The params in ' + function_check['id'] + ' are wrong')
    exit(0)

def add_function_to_global_variables(function_id, function_type):
  current_function['id'] = function_id
  current_function['type'] = function_type
  add_var_to_dict(function_id, function_type, False, None , 'global')

def add_function_var_to_stack():
  types_stack.append(var_dict['global'][current_function['id']]['type'])
  operand_stack.append(var_dict['global'][current_function['id']]['address'])
  operator_stack.append('=')

def get_global_memory_needed():
  global_dict['global_memory_needed'] = variable_counts(global_segment[0] - 40000, global_segment[1] - 42500, 
                                                       global_segment[2] - 45000, global_segment[3] - 47500,
                                                       0, 0, 0, 0)

def get_memory_needed_for_function():
  return variable_counts(function_segment[0] - 10000, function_segment[1] - 12500, function_segment[2] - 15000, function_segment[3] - 17500,
                         fun_temp_segment[0] - 50000, fun_temp_segment[1] - 52500, fun_temp_segment[2] - 55000, fun_temp_segment[3] - 57500)

def update_funct_memory(function_id, function_memory_needed):
  funct_dict[function_id]['memory_needed'] = function_memory_needed

def last_return(value):
  current_function['last_return'] = value

############################# LISTS METHODS ####################################

def add_list_variable(var_id):
  current_list.append({'id' : var_id, 'start_address' : None })

def add_list_index_to_stack():
  list_options = current_list[len(current_list) - 1]
  generate_ver_quadruple(list_options['id'])
  generate_list_index(list_options['id'])
  current_list.pop()

def generate_list_index(var_id):
  operator_stack.append('+')
  if not(str(var_dict[var_options['scope']][var_id]['address']) in var_dict['constants']):
    add_constant_to_dict_aux(str(var_dict[var_options['scope']][var_id]['address']), 'int')
  operand_stack.append(var_dict['constants'][str(var_dict[var_options['scope']][var_id]['address'])]['address'])
  types_stack.append(types['int'])
  generate_operations_quadruples(var_options['scope'], var_dict[var_options['scope']][var_id]['type'])