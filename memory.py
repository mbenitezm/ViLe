from numpy import *

class Memory:
  def __init__(self, name, memory_needed):
    function_name = name
    main_segment = numpy.empty((memory_needed['int'], dtype=int))

  def assign_real_address(self, type, virtual_address):

  def get_variable_scope(virtual_address):
    if virtual_address >= 0 && virtual_address < 10000:
      return "main"
    elif virtual_address >= 10000 && virtual_address < 20000:
      return "function"
    elif virtual_address >= 20000 && virtual_address < 30000:
      return "temp"
    elif virtual_address >= 40000 && virtual_address < 50000:
      return "global"
    elif virtual_address >= 50000 && virtual_address < 60000:
      return "fun_temp"

