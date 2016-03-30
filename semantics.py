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
  'void' : 5
}

var_dict = {
    'global' : {
     },
    'function' : {
    }
}

var_options = {
  'id' : None,
  'scope' : 'global',
  'type' : 'none',
}

funct_options = {
  'id' : None,
  'type' : 'none',
  'params' : {}
}

quadruplets = deque([])

operand_stack = []
operator_stack = []
types_stack = []


# Memory segment int float  bool  string
global_segment = [0, 2500, 5000, 7500]
function_segment = [10000, 12500, 15000, 17500]
temp_segment = [20000, 22500, 25000, 27500]

def add_global_memory(var_type):
    if var_type == 'int':
      if global_segment[0] > 2499:
        print('Memory overflow')
        exit(-1)
      else: 
        global_segment[0] += 1
    elif var_type == 'float':
      if global_segment[1] > 4999:
        print('Memory overflow')
        exit(-1)
      else:
        global_segment[1] += 1
    elif var_type == 'bool':
      if global_segment[2] > 7499:
        print('Memory overflow')
        exit(-1)
      else:
        global_segment[2] += 1
    elif var_type == 'string':
      if global_segment[3] > 9999:
        print('Memory overflow')
        exit(-1)
      else:
        global_segment[3] += 1

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
    
def add_temp_memory():
  temp_segment+=1

def realease_temp_memory():
  temp_segment-=1
################################################################################

def print_var_dict():
  print "\nVAR DICT"
  pp.pprint(var_dict)

def print_funct_dict():
  print "\nFUNCT DICT"
  pp.pprint(funct_dict)

def semantic_dict_constr():
  return { 
          'int' : { 
            'int' : op_constr('int', 'int', 'int', 'int', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error'),
            'float' : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error'),
            'string' : op_error(),
            'bool' : op_error()
          },
          'float' : { 
            'int' : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error'),
            'float' : op_constr('float', 'float', 'float', 'float', 'bool', 'bool', 'bool', 'bool', 'bool', 'error', 'error'),
            'string' : op_error(),
            'bool' : op_error()
          },
         'string' : { 
            'int' : op_error(),
            'float' : op_error(),
            'string' : op_constr('sring', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'error', 'error'),
            'bool' : op_error()
          },
          'bool' : { 
            'int' : op_error(),
            'float' : op_error(),
            'string' : op_error(),
            'bool' : op_constr('error', 'error', 'error', 'error', 'error', 'error', 'error', 'error', 'bool', 'bool', 'bool')
          }
         }

def op_constr(plus, minus, mult, div, greater_than, greater_eq_than, less_than, less_eq_than, equals, and_o, or_o):
  return { '+' : plus, '-' : minus, '*' : mult, '/' : div, '>' : greater_than, '>=' : greater_eq_than,
    '<' : less_than, '<=' : less_eq_than, '==' : equals, 'and' : and_o, 'or' : or_o}

def op_error():
  return { '+' : 'error', '-' : 'error', '*' : 'error', '/' : 'error', '>' : 'error', '>=' : 'error',
    '<' : 'error', '<=' : 'error', '==' : 'error', 'and' : 'error', 'or' : 'error'}

semantic_dict = semantic_dict_constr()

def add_var_to_dict(var_id, var_type, scope):
  address = assign_address(scope, var_type)

  var_dict[scope][var_id] = {
    'type': types[var_type],
    'address' : address
  }
  print_var_dict()

def assign_address(scope, var_type):
  if scope == 'global':
    if var_type == 'int':
      address = global_segment[0]
    elif var_type == 'float':
      address = global_segment[1]
    elif var_type == 'bool':
      address = global_segment[2]
    elif var_type == 'string':
      address = global_segment[3]
    add_global_memory(var_type)
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
  return address


def add_funct_to_dict(funct_id, funct_type, funct_params):
  funct_dict[funct_id] = {
      'type' : types[funct_type],
      'params' : funct_params
  }
  print_funct_dict()

def var_exists(var_id, scope):
  if var_id in var_dict[scope]:
    return True
  else:
    if var_id in var_dict['global']:
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
    'scope' : 'global',
    'type' : 'none',
  }

def add_main_to_dict():
  add_funct_to_dict('main', 'void', {})

def clean_funct_options():
  funct_options = {
    'id' : None,
    'type' : 'none',
    'params' : {}
  }