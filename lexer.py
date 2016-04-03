# -*- coding: utf-8 -*-
# Analizador léxico de ViLe
# Marcel Benítez Martínez 1139855
# Abraham Rodríguez

import ply.lex as lex

# Palabras reservadas
reserved = {
  # Palabras reservadas para funciones
  'def'    : 'FUNCTION',
  'main'   : 'MAIN',
  'return' : 'RETURN',
  'void'   : 'VOID',
  # Palabras reservadas para estatutos
  'if'     : 'IF',
  'else'   : 'ELSE',
  'print'  : 'PRINT',
  'while'  : 'WHILE',
  'times'  : 'TIMES',
  # Palabras reservadas para tipos de datos
  'int'    : 'INT',
  'float'  : 'FLOAT',
  'string' : 'STRING',
  'list'   : 'LIST',
  'bool'   : 'BOOL',
  # Palabras reservadas para operadores lógicos
  'true'   : 'TRUE',
  'false'  : 'FALSE',
  'and'    : 'AND',
  'or'     : 'OR'

}

# Declaracion de tokens
tokens = ('FUNCTION', 'MAIN', 'RETURN', 'VOID', 'IF', 'ELSE', 'PRINT',
          'WHILE', 'TIMES', 'INT', 'FLOAT', 'STRING', 'LIST', 'BOOL', 'TRUE',
          'FALSE', 'AND', 'OR', 'MINUS', 'SUM', 'MULTIPLY', 'DIVIDE', 'MOD',
          'EQUALS', 'EQUALITY', 'GREATER', 'LESS', 'GREATER_EQUAL',
          'LESS_EQUAL', 'DIFFERENT', 'SEMICOLON', 'COMMA',
          'O_PARENTHESIS', 'C_PARENTHESIS', 'O_BRACKET', 'C_BRACKET',
          'O_S_BRACKET', 'C_S_BRACKET','STRINGCONST', 'INTCONST', 'FLOATCONST',
          'ID' )

# Definicion de tokens
# Operadores y delimitadores
t_ignore = ' \t'
t_SUM = '\+'
t_MINUS = '-'
t_MULTIPLY = '\*'
t_DIVIDE = '/'
t_MOD = '%'
t_EQUALS = '='
t_EQUALITY = '=='
t_GREATER = '>'
t_LESS = '<'
t_GREATER_EQUAL = '>='
t_LESS_EQUAL = '<='
t_DIFFERENT = '!='
t_SEMICOLON = ';'
t_COMMA = ','
t_O_PARENTHESIS = '\('
t_C_PARENTHESIS = '\)'
t_O_BRACKET = '\{'
t_C_BRACKET = '\}'
t_O_S_BRACKET = '\['
t_C_S_BRACKET = '\]'
# Expresiones regulares
t_STRINGCONST = '".*"'
t_INTCONST = '-?[0-9]+'
t_FLOATCONST = '-?[0-9]+\.+[0-9]+'

# Contador de líneas de código
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Se revisan palabras reservadas
def t_ID(t):
  '[a-zA-Z]+[0-9]*(_[a-zA-Z0-9]+)?'
  t.type = reserved.get(t.value, 'ID')
  return t

#Error en léxico
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  exit(-1)
  t.lexer.skip(1)

lexer = lex.lex()
