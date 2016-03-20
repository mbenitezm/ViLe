# -*- coding: utf-8 -*-
import pprint
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
  var_dict[scope][var_id] = {
    'type': types[var_type]
  }
  print_var_dict()

# def add_proc_to_dict(proc_id, proc_type, proc_params, proc_address):
#   proc_dict[proc_id] = {
#       'type' : proc_type,
#       'params' : proc_params,
#       'address' : proc_address
#   }

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