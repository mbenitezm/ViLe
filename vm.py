# -*- coding: utf-8 -*-
# Memoria virtual
from memory import *
from semantics import *
from math import *

# Función de la memoria virtual encargada de resolver los cuádruplos generados
def solve():
  current_quadruple = 0
  alive_memory = Memory('main', funct_dict['main']['memory_needed']) 

  while quadruplets[current_quadruple][0] != 'ENDALL':
    quadruplet = quadruplets[current_quadruple]
    if quadruplet[0] == '+':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      op1 = alive_memory.get_value_from_real_address(type1, op1)
      op2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op1 + op2
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '-':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      op1 = alive_memory.get_value_from_real_address(type1, op1)
      op2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op1 - op2
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '*':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      op1 = alive_memory.get_value_from_real_address(type1, op1)
      op2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op1 * op2
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '/':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = operand1 / operand2
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
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = math.fmod(operand1, operand2)
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '>':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 > op1
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '<':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 < op1
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '>=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 >= op1
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '<=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 <= op1
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '==':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 == op1
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
      operand1 = alive_memory.get_value_from_real_address(type1, op1)
      operand2 = alive_memory.get_value_from_real_address(type2, op2)
      result = op2 != op1
      alive_memory.assign_to_real_address(type3, res, result)
      current_quadruple += 1

    elif quadruplet[0] == '=':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      res = quadruplet[4]
      type3 = quadruplet[5]
      result = alive_memory.get_value_from_real_address(type1, op1)
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
    elif quadruplet[0] == 'print':
      op1 = quadruplet[3]
      type1 = quadruplet[4]
      result = alive_memory.get_value_from_real_address(type1, op1)
      print result
      current_quadruple += 1