# -*- coding: utf-8 -*-
# Memoria virtual
from memory import *
from semantics import *
from math import *

# Función de la memoria virtual encargada de resolver los cuádruplos generados
def solve():
  # Cuádruplo inicial
  current_quadruple = 0
  # Inicializar memoria global
  global_memory = Memory('global', global_dict['global_memory_needed'])
  # Inicializar memoria del main y asignarla como viva
  alive_memory = Memory('main', funct_dict['main']['memory_needed'])
  waking_memory = None
  # Stack de memoria
  memory_stack = []
  # Stack de retorno
  returns_stack = []
  # Stack de ciclos
  current_loop_count = []
  # Mientras que no sea el final del programa
  while quadruplets[current_quadruple][0] != 'ENDALL':
    quadruplet = quadruplets[current_quadruple]
    # Caso para cuando es suma
    if quadruplet[0] == '+':
      op1 = quadruplet[1]
      type1 = quadruplet[2]
      op2 = quadruplet[3]
      type2 = quadruplet[4]
      res = quadruplet[5]
      type3 = quadruplet[6]

      # Se extrae la información de los cuádruplos y se consigue y asigna los valores
      # a la memoria real que le corresponde
      if is_global(op1):
        # Conseguir el valor guardado en la memoria real de global para operando1
        operand1 = global_memory.get_value_from_real_address(type1, op1)
      else:
        if op1 < 0:
          # Conseguir el valor guardado en la memoria real de la función. En este caso es un índice de una lista,
          # por lo que se tiene que acceder primero a su dirección indirecta y luego a la directa.
          operand1 = alive_memory.get_value_from_real_address(type1, -op1)
          operand1 = alive_memory.get_value_from_real_address(type1, operand1)
        else:
          # Conseguir el valor guardado en la memoria real de la función
          operand1 = alive_memory.get_value_from_real_address(type1, op1)

      # Se repite lo mismo que antes pero con el operando 3
      if is_global(op2):
        operand2 = global_memory.get_value_from_real_address(type2, op2)
      else:
        if op2 < 0:
          operand2 = alive_memory.get_value_from_real_address(type2, -op2)
          operand2 = alive_memory.get_value_from_real_address(type2, operand2)
        else:
          operand2 = alive_memory.get_value_from_real_address(type2, op2)

      result = operand1 + operand2

      # Asignar el resultado a la memoria real de la función
      if res < 0:
        real_res = alive_memory.get_value_from_real_address(type3, -res)
        alive_memory.assign_to_real_address(type3, real_res, result)
      else:
        alive_memory.assign_to_real_address(type3, res, result)

      # Se pasa al siguiente cuádruplo
      current_quadruple += 1
    
    # Caso para resta
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

    # Caso para multiplicación
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

    # Caso para división
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

    # Caso para mod
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
    
    # Caso para mayor que
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

    # Caso para menor que
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

    # Caso para mayor o igual que
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

    # Caso para menor o igual que
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

   # Caso para igual que
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

    # caso para and
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

    # Caso para or
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

    # Caso para diferente a
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

    # Caso para asignación
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

    # Caso para goto
    elif quadruplet[0] == 'GOTO':
      current_quadruple = quadruplet[3]
      if len(current_loop_count) > 0:
        current_loop_count[len(current_loop_count) - 1] += 1
        if current_loop_count[len(current_loop_count) - 1] > 100000:
          print "Cycle is infinite or too big."
          exit(0)

    # Caso para gotof
    elif quadruplet[0] == 'GOTOF':
      result = alive_memory.get_value_from_real_address(4, quadruplet[1])
      jump_to = quadruplet[3]
      if result == False:
        current_quadruple = jump_to
      else:
        current_quadruple += 1

    # Caso para ir a subrutina
    elif quadruplet[0] == 'GOSUB':
      # Se agrega al jumo stack el cuádruplo al que se regresará cuando termine la función
      jumps_stack.append(current_quadruple + 1)
      # Se tiene un límite de stack de recursividad
      if len(jumps_stack) > 1000:
        print "Stack too deep"
        exit(0)
      # Se va a la dirección de inicio de la función
      jump_to = funct_dict[function_name]['start']
      # La memoria que está viva actualmente de va a dormir, y entra la memoria de la función
      current_quadruple = jump_to
      memory_stack.append(alive_memory)
      alive_memory = waking_memory

    # Caso para return
    elif quadruplet[0] == 'RETURN':
      current_quadruple = jumps_stack.pop()
      alive_memory = memory_stack.pop()

    # Caso para finalización inesperada de uan función
    elif quadruplet[0] == 'ENDFUNCTION':
      print "You must return something in the function."
      exit(0)

    # Caso para era
    elif quadruplet[0] == 'ERA':
      function_name = quadruplet[3]
      # Se crea una nueva instancia de memoria con la memoria requerida y se asiga como
      # Memoria que se va despertando
      memory_for_function = funct_dict[function_name]['memory_needed']
      waking_memory = Memory(function_name, memory_for_function)
      # Se pasa al siguiente cuádruplo
      current_quadruple += 1
 
    # Caso para param
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

    # Caso para verificar índices de arreglo que se quiere acceder 
    elif quadruplet[0] == 'VER':
      if (quadruplet[1] < quadruplet[2] and quadruplet[1] > quadruplet[3]):
        print "List index out of rage"
        exit(0)
      current_quadruple += 1

    # Caso para print
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

   # Caso para inicio de while
    elif quadruplet[0] == 'WHILE':
      current_loop_count.append(0)
      current_quadruple += 1

   # Caso para finalización de while
    elif quadruplet[0] == 'ENDWHILE':
      current_loop_count.pop()
      current_quadruple += 1

# Verifica si la memoria virtual corresponde al sector global
def is_global(virtual_memory):
  return virtual_memory >= 40000 and virtual_memory < 50000