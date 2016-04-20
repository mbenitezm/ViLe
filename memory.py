# -*- coding: utf-8 -*-
from semantics import *
# Clase que maneja el mapeo de memoria del lenguaje.
class Memory:
  # Se inicializa una instancia de la clase memoria. Se le asigna el nombre de
  # la función y se asigna memoria dependiendo de la memoria que esta función
  # haya marcado que necesite por variable.
  def __init__(self, name, memory_needed):
    self.function_name = name
    # Memoria de la función
    self.integers = [[None]] * memory_needed['int']
    self.floats = [[None]] * memory_needed['float']
    self.bools = [[None]] * memory_needed['bool']
    self.strings = [[None]] * memory_needed['string']
    #Memoria temporal de la función
    self.temp_integers = [[None]] * memory_needed['temp_int']
    self.temp_floats = [[None]] * memory_needed['temp_float']
    self.temp_bools = [[None]] * memory_needed['temp_bool']
    self.temp_strings = [[None]] * memory_needed['temp_string']
  
  # Regresa lo que esté guardado dentro de la dirección real de la variable
  def get_value_from_real_address(self, type, virtual_address):
    scope = self.get_variable_scope(virtual_address)[0]
    if scope != 'const':
      offset = self.get_variable_scope(virtual_address)[1]
      offset += self.get_type_offset(type)
      corresponding_memory = self.get_corresponding_memory(scope, type)
      real_address = virtual_address - offset
      return corresponding_memory[real_address]
    else:
      return var_dict['inverse_constants'][virtual_address]['value']

  # Asigna un valor a la memoria real de una variable
  def assign_to_real_address(self, type, virtual_address, value):
    scope = self.get_variable_scope(virtual_address)[0]
    offset = self.get_variable_scope(virtual_address)[1]
    offset += self.get_type_offset(type)
    corresponding_memory = self.get_corresponding_memory(scope, type)
    real_address = self.get_real_address(type, virtual_address)
    corresponding_memory[real_address] = value

  # Regresa el valor real de la dirección de memoria real
  def get_real_address(self, type, virtual_address):
    scope = self.get_variable_scope(virtual_address)[0]
    offset = self.get_variable_scope(virtual_address)[1]
    offset += self.get_type_offset(type)
    corresponding_memory = self.get_corresponding_memory(scope, type)
    return virtual_address - offset

  # Esta función simplemente regresa a que parte del programa pertenece la
  # variable, y su offset para poder acceder a su dirección real.
  def get_variable_scope(self, virtual_address):
    if virtual_address >= 0 and virtual_address < 10000:
      return ["main", 0]
    elif virtual_address >= 10000 and virtual_address < 20000:
      return ["function", 10000]
    elif virtual_address >= 20000 and virtual_address < 30000:
      return ["temp", 20000]
    elif virtual_address >= 30000 and virtual_address < 40000:
      return ["const", 30000]
    elif virtual_address >= 40000 and virtual_address < 50000:
      return ["global", 40000]
    elif virtual_address >= 50000 and virtual_address < 60000:
      return ["fun_temp", 50000]

  # Regresa el offset de la memoria virtual generado por el tipo de dato
  def get_type_offset(self, type):
    if type == 1:
      return 0
    elif type == 2:
      return 250
    elif type == 3:
      return 750
    elif type == 4:
      return 500

  # Esta función regresa el bloque de memoria al que pertenece la variable
  def get_corresponding_memory(self, scope, type):
    if scope == 'main' or scope == 'function':
      if type == 1:
        return self.integers
      elif type == 2:
        return self.floats
      elif type == 3:
        return self.strings
      elif type == 4: 
        return self.bools
    elif scope == 'temp' or scope == 'fun_temp':
      if type == 1:
        return self.temp_integers
      elif type == 2:
        return self.temp_floats
      elif type == 3:
        return self.temp_strings
      elif type == 4: 
        return self.temp_bools
