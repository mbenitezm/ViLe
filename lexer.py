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
  'var'    : 'VAR',
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
tokens = ( 'PROGRAM', 'IF', 'ELSE', 'VAR', 'PRINT','COMA' ,'PUNTOCOMA', 'DOSPUNTOS',
           'IGUAL', 'APARENTESIS', 'CPARENTESIS', 'ABRAQUET', 'CBRAQUET',
           'MAYOR', 'MENOR', 'IGUALDAD', 'PUNTO', 'SUMA', 'RESTA', 'MULT',
           'DIV', 'ID', 'INT', 'FLOAT','CTESTRING', 'CTEINT', 'CTEFLOAT' )

# Definicion de tokens
# Operadores y delimitadores
t_ignore = ' \t\n'
t_SUM = '+'
t_MINUS = '-'
T_MULTIPLY = '*'
T_DIVIDE = '/'
T_MOD = '%'
T_EQUALS = '='
T_EQUIALITY = '=='
T_GREATER = '>'
T_LESS = '<'
T_GREATER_EQUAL = '>='
T_LESS_EQUAL = '<='
T_DIFFERENT = '!='
T_SEMICOLON = ';'
T_COLON = ':'
T_COMA = ','
T_O_PARENTHESIS = '('
T_C_PARENTHESIS = ')'
T_O_BRACKET = '{'
T_C_BRACKET = '}'
T_O_S_BRACKET = '['
T_O_C_BRACKET = ']'
# Expresiones regulares
T_STRINGCONST = '"-*"'
T_INTCONST = '-?[0-9]+'
T_FLOATCONST = '-?[0-9]+.+[0-9]+'
T_ID = '[a-zA-Z]+(_?[a-zA-Z0-9])*'

#Se revisan palabras reservadas
def t_ID(t):
  '[a-zA-Z]+[0-9]*(_[a-zA-Z0-9]+)?'
  t.type = reserved.get(t.value, 'ID')
  return t

#Error en lexico
def t_error(t):
  print "Error in token ", t
  exit(-1)
  t.lexer.skip(1)


lexer = lex.lex()