# -*- coding: utf-8 -*-
# Memoria virtual
from memory import *
from semantics import *
from math import *

# Función de la memoria virtual encargada de resolver los cuádruplos generados
def solve():
  current_quadruple = 0
  global_memory = Memory('global', global_dict['global_memory_needed'])
  alive_memory = Memory('main', funct_dict['main']['memory_needed'])
  waking_memory = None
  memory_stack = []
  returns_stack = []

  while quadruplets[current_quadruple][0] != 'ENDALL':
    quadruplet = quadruplets[current_quadruple]
    if quadruplet[0] == '+':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 + operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '-':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 - operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '*':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 * operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '/':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 / operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    # Agregar a cubo
    elif quadruplet[0] == '%':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 % operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '>':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 > operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '<':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 < operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '>=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 >= operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '<=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 <= operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '==':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 == operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == 'and':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 and operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == 'or':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 or operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    # Agregar a cubo
    elif quadruplet[0] == '!=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      if is_global(op1):
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 != operand2

      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      current_quadruple += 1

    elif quadruplet[0] == '=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      res = quadruplet[4]
      type3 = quadruplet[5]

      if is_global(op1):
        result = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          result = alive_memory.get_value_from_real_address(type1, -op1)
          result = alive_memory.get_value_from_real_address(type1, result)
        else:
          result = alive_memory.get_value_from_real_address(type1, op1)
      if is_global(res):
        global_memory.assign_to_real_address(type3, res, result)
      else:
        if res < 0:
          real_res = alive_memory.get_value_from_real_address(type3, -res)
          alive_memory.assign_to_real_address(type3, real_res, result)
        else:
          alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == 'GOTO':
      current_quadruple = quadruplet[3]

    elif quadruplet[0] == 'GOTOF':
      result = alive_memory.get_value_from_real_address(4, quadruplet[1])
      jump_to = quadruplet[3]
      if result == False:
        current_quadruple = jump_to
      else:
        current_quadruple += 1

    elif quadruplet[0] == 'GOSUB':
      jumps_stack.append(current_quadruple + 1)
      if len(jumps_stack) > 1000:
        print "Stack too deep"
        exit(0)
      jump_to = funct_dict[function_name]['start']
      current_quadruple = jump_to
      memory_stack.append(alive_memory)
      alive_memory = waking_memory

    elif quadruplet[0] == 'RETURN':
      current_quadruple = jumps_stack.pop()
      alive_memory = memory_stack.pop()

    elif quadruplet[0] == 'ENDFUNCTION':
      print "You must return something in the function."
      exit(0)

    elif quadruplet[0] == 'ERA':
      function_name = quadruplet[3]
      memory_for_function = funct_dict[function_name]['memory_needed']
      waking_memory = Memory(function_name, memory_for_function)
      current_quadruple += 1
 
    elif quadruplet[0] == 'PARAM':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      res = quadruplet[4]
      type3 = quadruplet[5]
      if is_global(op1):
        result = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          result = alive_memory.get_value_from_real_address(type1, -op1)
          result = alive_memory.get_value_from_real_address(type1, result)
        else:
          result = alive_memory.get_value_from_real_address(type1, op1)
     
      waking_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == 'VER':
      if (quadruplet[1] < quadruplet[2] and quadruplet[1] > quadruplet[3]):
        print "List index out of rage"
        exit(0)
      current_quadruple += 1

    elif quadruplet[0] == 'print':
      op1 = quadruplet[3]
      type1 = quadruplet[4]

      if is_global(op1):
        result = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          result = alive_memory.get_value_from_real_address(type1, -op1)
          result = alive_memory.get_value_from_real_address(type1, result)
        else: 
          result = alive_memory.get_value_from_real_address(type1, op1)

      print result
      current_quadruple += 1


def is_global(virtual_memory):
  return virtual_memory >= 40000 and virtual_memory < 50000