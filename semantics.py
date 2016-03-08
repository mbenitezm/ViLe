# The pprint module provides a capability to “pretty-print” arbitrary Python 
# data structures in a form which can be used as input to the interpreter. 
# If the formatted structures include objects which are not fundamental 
# Python types, the representation may not be loadable. 
import pprint
pp = pprint.PrettyPrinter()

###### Initialize structures ###################################################

proc_dict = {}
var_dict = {
    'global' : {
     },
    'local' : {
    }
}

################################################################################

def print_var_dict():
  print "\nVAR DICT"
  pp.pprint(local_var_dict)

def print_proc_dict():
  print "\nPROC DICT"
  pp.pprint(local_var_dict)

def add_var_to_dict(address, var_id, size, scope):
    var_dict[scope][address] = {
        'id': var_id,
        'size': size
    }
    print_var_dict()

def add_proc_to_dict(proc_id, proc_type, proc_params, proc_address):
  func_dict[proc_id] = {
      'type' : proc_type,
      'params' : proc_params,
      'address' : proc_address
  }