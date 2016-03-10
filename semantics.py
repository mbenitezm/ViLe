# -*- coding: utf-8 -*-
import pprint
pp = pprint.PrettyPrinter()

###### Initialize structures ###################################################
types = {
  'int' : 1,
  'float' : 2,
  'string' : 3,
  'bool' : 4 ,
  'void' : 5
}
proc_dict = {}
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

fun_options = {
  
}

################################################################################

def print_var_dict():
  print "\nVAR DICT"
  pp.pprint(var_dict)

def print_proc_dict():
  print "\nPROC DICT"
  pp.pprint(local_var_dict)

def add_var_to_dict(var_id, var_type, scope):
    var_dict[scope][var_id] = {
        'type': types[var_type]
    }
    print_var_dict()

def add_proc_to_dict(proc_id, proc_type, proc_params, proc_address):
  proc_dict[proc_id] = {
      'type' : proc_type,
      'params' : proc_params,
      'address' : proc_address
  }

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
