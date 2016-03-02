import ply.yacc as yacc
import lex
tokens = lex.tokens

def p_program(p):
  '''program : main functionloop'''
  p[0] = "Valid"

def p_main(p):
  '''main : MAIN block'''

def p_functionloop(p):
  ''' functionloop : function functionloop  
                   |'''

def p_function(p):
  ''' function : FUNCTION functiontype ID O_PARENTHESIS parameters C_PARENTHESIS block'''

def p_functiontype(p):
  ''' functiontype : VOID
                   | type'''

def p_type(p):
  ''' type : BOOL
           | INT
           | FLOAT
           | STRING'''

def p_block(p):
  ''' block : O_BRACKET statutesloop C_BRACKET'''

def p_statutesloop(p):
  ''' statutesloop : statute statutesloop
                   |'''

def p_statute(p):
  ''' statute : init
              | condition
              | writting
              | loop
              | assignation
              | functioncall'''

def p_assignation(p):
  ''' assignation : var EQUALS expression SEMICOLON'''

def p_writting(p):
  ''' writting :  PRINT O_PARENTHESIS writtingloop C_PARENTHESIS SEMICOLON'''

def p_writtingloop(p):
  ''' writtingloop : expression optionalwritting'''

def p_optionalwritting(p):
  ''' optionalwritting : COMMA writtingloop
                       |'''

def p_init(p):
  ''' init : listinit
           | normalinit'''

def p_normalinit(p):
  ''' normalinit : type var EQUALS expression SEMICOLON'''

def p_listinit(p):
  ''' listinit : LIST type var EQUALS list SEMICOLON'''

def p_list(p):
  ''' list : O_S_BRACKET listelements C_S_BRACKET'''

def p_listelements(p):
  ''' listelements : constants optionalconstants 
                   |'''

def p_optionalconstants(p):
  ''' optionalconstants : COMMA constants optionalconstants
                        |'''

def p_condition(p):
  ''' condition : IF O_PARENTHESIS expression C_PARENTHESIS block else'''

def p_else(p):
  ''' else : ELSE block
           |'''

def p_expression(p):
  ''' expression : expression2 expressionoptional'''

def p_expressionoptional(p):
  ''' expressionoptional : logicop expression2
                         |'''

def p_expression2(p):
  ''' expression2 : exp expression2optional'''

def p_expression2optional(p):
  ''' expression2optional : relop exp
                          |'''

def p_logicop(p):
  ''' logicop : AND
              | OR'''

def p_relop(p):
  ''' relop : EQUALITY
            | GREATER
            | GREATER_EQUAL
            | LESS
            | LESS_EQUAL
            | DIFFERENT'''

def p_exp(p):
  ''' exp : term exploop'''

def p_exploop(p):
  ''' exploop : addsub exp
              |'''

def p_addsub(p):
  ''' addsub : SUM
             | MINUS'''

def p_term(p):
  ''' term : fact termloop'''

def p_termloop(p):
  ''' termloop : divmult term
               |'''

def p_divmult(p):
  ''' divmult : MULTIPLY
              | DIVIDE'''

def p_fact(p):
  ''' fact : varconst
           | O_PARENTHESIS expression C_PARENTHESIS'''

def p_var(p):
  ''' var : ID listaccess'''

def p_listaccess(p):
  ''' listaccess : O_S_BRACKET INTCONST C_S_BRACKET
                 |'''

def p_varconst(p):
  ''' varconst : var
               | constants
               | functioncall'''

def p_constants(p):
  ''' constants : INTCONST
                | FLOATCONST
                | STRINGCONST
                | booleanconst'''

def p_booleanconst(p):
  ''' booleanconst : TRUE
                   | FALSE'''

def p_loop(p):
  ''' loop : whileloop
           | timesloop'''

def p_whileloop(p):
  ''' whileloop : while O_PARENTHESIS expression C_PARENTHESIS block'''

def p_timesloop(p):
  ''' timesloop : TIMES O_PARENTHESIS INTCONST C_PARENTHESIS block'''

def p_functioncall(p):
  ''' functioncall : ID O_PARENTHESIS parametersinput C_PARENTHESIS SEMICOLON'''

def p_parametersinput(p):
  ''' parametersinput : expression parametersinputloop
                      |'''

def p_parametersinputloop(p):
  ''' parametersinputloop : COMMA expression parametersinputloop
                         |'''

def p_parameters(p):
  ''' parameters : type ID parametersloop
                 |'''

def p_parametersloop(p):
  ''' parametersloop : COMMA type ID parametersloop
                     |'''

def p_error(p):
    if type(p).__name__ == 'NoneType':
      print('Syntax error')
    else:
      print('Syntax error at token', p.type, p.value)
# Build the parser
parser = yacc.yacc(start='program')

def check(filename):
  f = open(filename, 'r')
  data = f.read()
  f.close()
  if parser.parse(data) == 'Valid':
    print('VALID!')