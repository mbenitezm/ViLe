  # -*- coding: utf-8 -*-
import pprint
from collections import deque
pp = pprint.PrettyPrinter()

###### Initialize structures ###################################################

funct_dict = {}

types = {
  'int' : 1,
  'float' : 2,
  'string' : 3,
  'bool' : 4 ,
  'void' : 5,
  'error': -1
}

var_dict = {
    'main' : {
     },
    'function' : {
    },
    'constants' : {
    }
}

var_options = {
  'id' : None,
  'scope' : 'main',
  'type' : None,
}

funct_options = {
  'id' : None,
  'type' : None,
  'params' : {},
  'params_order' : ''
}

quadruplets = deque([])

operand_stack = []
operator_stack = []
types_stack = []


# Memory segment int float  bool  string
main_segment = [0, 2500, 5000, 7500]
function_segment = [10000, 12500, 15000, 17500]
temp_segment = [20000, 22500, 25000, 27500]
const_segment = [30000, 32500, 35000, 37500]

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
  if var_type == 0:
    if temp_segment[0] > 22499:
      print('Memory overflow')
      exit(-1)
    else: 
      const_segment[0] += 1
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
    
def add_temp_memory():
  temp_segment+=1

def realease_temp_memory():
  temp_segment-=1
########################Quadruple Generation####################################
def generate_operations_quadruples():
  type2 = types_stack.pop()
  type1 = types_stack.pop()
  operator1 = operator_stack.pop()
  result_type = semantic_dict[type1][type2][operator1]
  if result_type < 1:
    print type1, " and ", type2, " are not a valid type combination for ", operator1 
    exit(0)
  else:
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    result = assign_address('temp', result_type)
    quadruple = [operator1, operand1, operand2, result]
    operand_stack.append(result)
    types_stack.append(result_type)

def generate_equals_quadruples():
  type2 = types_stack.pop()
  type1 = types_stack.pop()
  operator1 = operator_stack.pop()
  result_type = semantic_dict[type1][type2][operator1]
  if result_type < 1:
    print type1, " and ", type2, " are not a valid type combination for ", operator1
    exit(0)
  else:
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    quadruple = [operator1, operand2, '',  operand1]
    operand_stack.append(operand1)
    types_stack.append(result_type)

def semantics_add_to_stack(id):
  if id in var_dict['function']:
    operand_stack.append(var_dict['function'][id]['address'])
    types_stack.append(var_dict['function'][id]['type'])
  elif id in var_dict['main']:
    operand_stack.append(var_dict['main'][id]['address'])
    types_stack.append(var_dict['main'][id]['type'])
  else:
    print id, " doesn't exists"
    exit(0)
  # TODO: AGREGAR QUE JALEN LAS FUNCIONES TAMBIEN

################################################################################
def print_var_dict():
  print "\nVAR DICT"
  pp.pprint(var_dict)

def print_funct_dict():
  print "\nFUNCT DICT"
  pp.pprint(funct_dict)

def semantic_dict_constr():
  return { 
          types['int'] : { 
            types['int'] : op_constr('int', 'int', 'int', 'int', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'int'),
            types['float'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'error'),
            types['string'] : op_error(),
            types['bool'] : op_error()
          },
          types['float'] : { 
            types['int'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'float'),
            types['float'] : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error', 'float'),
            types['string'] : op_error(),
            types['bool'] : op_error()
          },
         types['string'] : { 
            types['int'] : op_error(),
            types['float'] : op_error(),
            types['string'] : op_constr('string', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'error', 'error', 'string'),
            types['bool'] : op_error()
          },
          types['bool'] : { 
            types['int'] : op_error(),
            types['float'] : op_error(),
            types['string'] : op_error(),
            types['bool'] : op_constr('error', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'bool', 'bool', 'bool')
          }
         }

def op_constr(plus, minus, mult, div, greater_than, greater_eq_than, less_than, less_eq_than, equals, and_o, or_o, equal):
  return { '+' : types[plus], '-' : types[minus], '*' : types[mult], '/' : types[div], '>' : types[greater_than], '>=' : types[greater_eq_than],
    '<' : types[less_than], '<=' : types[less_eq_than], '==' : types[equals], 'and' : types[and_o], 'or' : types[or_o], '=' : types[equal]}

def op_error():
  return { '+' : types['error'], '-' : types['error'], '*' : types['error'], '/' : types['error'], '>' : types['error'], '>=' : types['error'],
    '<' : types['error'], '<=' : types['error'], '==' : types['error'], 'and' : types['error'], 'or' : types['error'], '=' : types['error']}

semantic_dict = semantic_dict_constr()

def add_var_to_dict(var_id, var_type, scope):
  address = assign_address(scope, var_type)

  var_dict[scope][var_id] = {
    'type': types[var_type],
    'address' : address
  }
  print_var_dict()

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
    elif var_type == 3:
      address = temp_segment[2]
    elif var_type == 4:
      address = temp_segment[3]
    add_temp_memory(var_type)
  return address

def add_constant_to_dict_aux(constant, type):
  print constant, type
  address = assign_address('constants', type)
  var_dict['constants'][constant] = {
    'address' : address,
    'type' : types[type]
  }

def add_funct_to_dict(funct_id, funct_type, funct_params, funct_params_order):
  funct_dict[funct_id] = {
      'type' : types[funct_type],
      'params' : funct_params,
      'params_order' : funct_params_order
  }
  print_funct_dict()

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
    if var_id in var_dict['main']:
      return True
    else:
      return False

def var_exists_expressions(var_id, scope):
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
  add_funct_to_dict('main', 'void', {}, '')

def clean_funct_options():
  funct_options = {
    'id' : None,
    'type' : None,
    'params' : {},
    'params_order' : ''
  }