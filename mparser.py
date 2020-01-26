# ==================================================================================================================
#  parser_v2.py                                                                                   
#  Analizador Sintactico - Compilador en Phyton para SQL92                                                                            
#  Construido por:
#                       Kenny Bedoya        1088305866
#                       Oscar Bernal        1088304958
#                       Sebastian Zapata    1088302207
#===================================================================================================================
from lexxer import tokens
import sys
import lexxer
import ply.yacc as yacc
#===================================================================================================================
# Reglas Gramaticales

def p_sql_list(p):
	''' sql_list : sql 
				       | sql_list sql'''
	pass

def p_sql(p):
    ''' sql : schema SEMICOLON
            | manipulative_statement SEMICOLON
            | func
            | WHENEVER NOT FOUND when_action SEMICOLON
            | WHENEVER SQLERROR when_action SEMICOLON
            '''
    pass

#===================================================================================================================
#Manipulacion de Statements como delete, select
def p_schema(p):
    'schema : CREATE SCHEMA AUTHORIZATION user opt_schema_element_list'
    pass
	
def p_user(p):
    'user : ID'
    pass

def p_opt_schema_element_list(p):
    '''opt_schema_element_list : schema_element_list
							   | empty'''
    pass
	
def p_schema_element_list(p):
    '''schema_element_list : schema_element
					      | schema_element_list schema_element'''
    pass
	
def p_schema_element(p):
    '''schema_element : base_table_def
						  | view_def
					      | privilege_def '''
    pass

def p_base_table_def(p):
    'base_table_def : CREATE TABLE ID LPAREN base_table_element_commalist RPAREN'
    pass

def p_table(p):
    '''table : ID
			| ID DOT ID'''
    pass

def p_base_table_element_commalist(p):
    '''base_table_element_commalist : base_table_element
			                        | base_table_element_commalist COMMA base_table_element'''
    pass

def p_base_table_element(p):
    '''base_table_element : column_def
			              | table_constraint_def'''
    pass

def p_column_def(p):
    'column_def : ID data_type column_def_opt_list'
    pass

	
def p_data_type(p):
    '''data_type : CHAR
				          | CHAR LPAREN NUMBER RPAREN
				          | VARCHAR 
				          | VARCHAR LPAREN NUMBER RPAREN
				          | INT
				          | INT LPAREN NUMBER RPAREN
				          | DATE 
                  | INT IDENTITY LPAREN ID COMMA ID RPAREN
                  | INT IDENTITY LPAREN NUMBER COMMA NUMBER RPAREN
                  | BIT 
                  | SMALLDATETIME'''
			  
    pass

def p_column_def_opt_list(p):
    '''column_def_opt_list : column_def_opt_list column_def_opt
						    | empty'''
    pass
	
def p_column_def_opt(p):
    ''' column_def_opt : NOT NULL
            | NULL
						| NOT NULL UNIQUE
						| NOT NULL PRIMARY KEY
						| DEFAULT NULL
						| DEFAULT USER
						| CHECK LPAREN search_condition RPAREN
						| REFERENCES ID
						| REFERENCES ID LPAREN column_commalist RPAREN '''
    pass

def p_table_constraint_def(p):
	''' table_constraint_def : UNIQUE LPAREN column_commalist RPAREN
							| CONSTRAINT ID PRIMARY KEY LPAREN column_commalist RPAREN
							| CONSTRAINT ID FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES ID
							| CONSTRAINT ID FOREIGN KEY LPAREN column_commalist RPAREN REFERENCES ID LPAREN column_commalist RPAREN 
							| CHECK LPAREN search_condition RPAREN '''
	pass

def p_column_commalist(p):
	'''column_commalist : ID
			            | column_commalist COMMA ID'''
	pass

def p_column(p):
    'column : ID'
    pass


def p_view_def(p):    
    'view_def : CREATE VIEW ID opt_column_commalist AS query_spec opt_with_check_option'
    pass
    
    
def p_opt_with_check_option(p):    
    '''opt_with_check_option : empty 
                              | WITH CHECK OPTION'''
    pass
    

def p_opt_column_commalist(p):
    '''opt_column_commalist : empty
                             | LPAREN column_commalist RPAREN '''
    pass

def p_privilege_def(p):
    'privilege_def : GRANT privileges ON table TO grantee_commalist opt_with_grant_option'       
    pass

def p_opt_with_grant_option(p):
    '''opt_with_grant_option : empty 
                              | WITH GRANT OPTION'''
    pass

def p_privileges(p):    
    '''privileges : ALL privileges
                   | ALL
                   | operation_commalist'''
    pass

def p_operation_commalist(p):
    '''operation_commalist : operation
                            | operation_commalist COMMA operation'''
    pass

def p_operation(p):
    '''operation : SELECT
                  | INSERT 
                  | DELETE
                  | UPDATE opt_column_commalist
                  | REFERENCES opt_column_commalist'''
    pass

def p_grantee_commalist(p):    
    '''grantee_commalist : grantee
                     | grantee_commalist COMMA grantee'''
    pass

def p_grantee(p):    
    '''grantee : PUBLIC
                | user'''
    pass

def p_cursor_def(p):
   'cursor_def : DECLARE ID CURSOR FOR query_exp opt_order_by_clause'
   pass

def p_opt_order_by_clause(p):
    '''opt_order_by_clause : empty 
                            | ORDER BY ordering_spec_commalist'''
    pass

def p_ordering_spec_commalist(p):
    '''ordering_spec_commalist : ordering_spec
                                 | ordering_spec_commalist COMMA ordering_spec'''
    pass

def p_ordering_spec(p):
    '''ordering_spec : NUMBER opt_asc_desc
                  | column_ref opt_asc_desc'''
    pass

def p_opt_asc_desc(p):
    '''opt_asc_desc : empty 
                 | ASC'''
    pass

def p_cursor(p):
    'cursor : ID'
    pass

def p_column_ref(p):
    '''column_ref : ID
                   | ID DOT ID
                   | ID DOT ID DOT ID'''
    pass

def p_manipulative_statement(p):
    '''manipulative_statement : close_statement
                             | commit_statement               
                             | delete_statement_positioned
                             | delete_statement_searched
                             | drop_statement_searched
                             | fetch_statement
                             | insert_statement
                             | open_statement
                             | rollback_statement
                             | select_statement
                             | update_statement_positioned
                             | update_statement_sarched 
                             | base_table_def '''
    pass

#===================================================================================================================
# Simples Statements

def p_open_statement(p):
    'open_statement : OPEN cursor'
    pass

def p_close_statement(p):
    'close_statement : CLOSE cursor'
    pass
                                          # COMMIT WORK 
def p_comnit_statement(p):
    'commit_statement : COMMIT WORK'
    pass
                                          #ROLLBACK 
def p_rollback_statement(p):
    'rollback_statement : ROLLBACK WORK'
    pass
                                           #CURRENT OF
def p_delete_statement_positioned(p):
    'delete_statement_positioned : DELETE FROM ID WHERE CURRENT OF cursor'
    pass

#===================================================================================================================
#Fetch Statement 

def p_fetch_statement(p):
    'fetch_statement : FETCH ID INTO target_commalist'
    pass

def p_target_commalist(p):
  '''target_commalist : target
                     | target_commalist COMMA target '''
  pass

def p_target(P):
    'target : parameter_ref'
    pass
                                   #INDICADOR
def p_parameter_ref(p):
    '''parameter_ref : parameter
                      | parameter parameter
                      | parameter INDICADOR parameter '''
    pass

def p_parameter(p):
    '''parameter : COLON ID
                  | ID '''
    pass

#===================================================================================================================
# Insert Statements

def p_insert_statement (p):
    'insert_statement : INSERT INTO ID opt_column_commalist  values_or_query_spec'
    pass

def p_values_or_query_spec(p):
    '''values_or_query_spec : VALUES LPAREN insert_atom_commalist RPAREN
                              | query_spec '''
    pass

def p_insert_atom_commalist(p):
    '''insert_atom_commalist : insert_atom
                              | insert_atom_commalist COMMA insert_atom '''
    pass

def p_insert_atom(p):
    '''insert_atom : ID
                    | NUMBER 
                    | string   
                    | NULL '''
    pass

def p_string(p):
    '''string : APOSTROPHE elemento APOSTROPHE
              | DOSCOMILLAS elemento DOSCOMILLAS'''
    pass

def p_elemento(p):
    '''elemento : ID
                | ID elemento
                | NUMBER
                | NUMBER elemento
                | MINUS
                | MINUS elemento'''
    pass

def p_atom(p):
    ''' atom : parameter_ref
            | insert_atom
            | USER '''
    pass

#===================================================================================================================
# Delete  Stataments pag 

def p_delete_statement_searched(p):
    'delete_statement_searched : DELETE FROM ID opt_where_clause'
    pass

def p_drop_statement_searched(p):
    'drop_statement_searched : DROP TABLE ID'
    pass

def p_opt_where_clause(p):
    ''' opt_where_clause : where_clause
                          | WHERE search_condition
                          | empty
                      '''
    pass

def p_where_clause(p):
    'where_clause : WHERE search_condition'
    pass

def p_update_statament_positioned(p):
    '''update_statement_positioned : UPDATE ID SET assignment_commanlist
                                   | WHERE CURRENT OF cursor '''
    pass

def p_assignment_commanlist(p):
    '''assignment_commanlist : assignment
                             | assignment_commanlist COMMA assignment '''
    pass

def p_assignment(p):
    '''assignment : ID EQUAL scalar_exp
                  | ID EQUAL string
                  | ID EQUAL NULL 
                  | ID EQUAL ID'''
    pass

def p_update_statement_sarched(p):
    'update_statement_sarched : UPDATE ID SET assignment_commanlist opt_where_clause'
    pass

#===================================================================================================================
# Scalar Expresions 

def p_scalar_exp(p):
   '''scalar_exp : scalar_exp PLUS scalar_exp
                 | scalar_exp MINUS scalar_exp
                 | scalar_exp TIMES scalar_exp
                 | scalar_exp DIVIDE scalar_exp
                 | atom
                 | ID
                 | APOSTROPHE ID APOSTROPHE
                 | LPAREN scalar_exp RPAREN '''
   pass
#| '+' scalar_exp %prec UMINUS
#| '-' scalar_exp %prec UMINUS


def p_scalar_exp_commalist(p):
    '''scalar_exp_commalist : scalar_exp
                            | scalar_exp_commalist COMMA scalar_exp '''
    pass


def p_select_statement(p):
    'select_statement : SELECT opt_all_distinct FROM target_commalist table_exp'
    pass

def p_opt_all_distinct(p):
    ''' opt_all_distinct : empty
                        | TIMES
                        | ALL  
                        | DISTINCT'''  #TIMES = '*'
    pass  

def p_query_exp(p):
	''' query_exp : query_term
					| query_exp UNION query_term
					| query_exp UNION ALL query_term '''
	pass

def p_query_term(p):
	''' query_term : query_spec
					| LPAREN query_exp RPAREN '''
	pass

def p_query_spec(p):
    'query_spec : SELECT opt_all_distinct table_exp'
    pass

def p_table_exp(p):
    '''table_exp : from_clause opt_where_clause opt_group_by_clause opt_having_clause
                  | opt_where_clause opt_group_by_clause opt_having_clause'''
    pass
	
def p_from_clause(p):
    'from_clause : FROM table_ref_commalist '
    pass
	
def p_table_ref_commalist(p):
    '''table_ref_commalist : table_ref_commalist COMMA table_ref
							| table_ref '''
    pass

def p_table_ref(p):
    '''table_ref : ID
				 | ID ID '''
    pass

def p_range_variable(p):
    'range_variable : ID '
    pass
	
def p_opt_group_by_clause(p):
    '''opt_group_by_clause : empty
						| GROUP BY column_ref_commalist '''
pass

def p_column_ref_commalist(p):
    '''column_ref_commalist : ID
						| column_ref_commalist COMMA ID '''
pass
	
def p_opt_having_clause(p):
    '''opt_having_clause : empty
						| HAVING search_condition '''
pass

def p_search_condition(p):
    '''search_condition :  search_condition OR search_condition
                      | search_condition AND search_condition
                      | search_condition AMPERSANT AMPERSANT search_condition GREATER NUMBER
                      | search_condition AMPERSANT AMPERSANT search_condition
                      | NOT search_condition
                      | LPAREN search_condition RPAREN
                      | search_condition
                      | predicate'''
    pass

def p_predicate(p):    
    '''predicate : comparison_predicate
              | between_predicate
              | like_predicate
              | test_for_null
              | in_predicate
              | all_or_any_predicate
              | existence_test
              | scalar_exp
              | assignment'''
    pass

def p_comparison_predicate(p):
    '''comparison_predicate : scalar_exp comparison_simbol scalar_exp
                         | scalar_exp comparison_simbol subquery'''
    pass

def p_between_predicate(p):
    '''between_predicate : scalar_exp NOT BETWEEN scalar_exp AND scalar_exp
                      | scalar_exp BETWEEN scalar_exp AND scalar_exp'''
    pass

def p_like_predicate(p):
    '''like_predicate : ID NOT LIKE atom opt_escape
                   | ID LIKE atom opt_escape'''
    pass

def p_opt_escape(p):
    '''opt_escape : empty 
               | ESCAPE atom'''
    pass

def p_test_for_null(p):
    '''test_for_null : ID IS NOT NULL
                  | ID IS NULL'''
    pass

def p_in_predicate(p):
    '''in_predicate : scalar_exp NOT IN LPAREN subquery RPAREN
                 |  scalar_exp IN LPAREN subquery RPAREN
                 |  scalar_exp NOT IN LPAREN atom_commalist RPAREN
                 |  scalar_exp IN LPAREN atom_commalist RPAREN '''
    pass

def p_atom_commalist(p):
    '''atom_commalist : atom
                   | atom_commalist COMMA atom'''
    pass

def p_all_or_any_predicate(p):
    'all_or_any_predicate : scalar_exp COMPARISON any_all_some subquery'
    pass
            
def p_any_all_some(p):
    '''any_all_some : ANY
                 | ALL
                 | SOME'''
    pass

def p_existence_test(p):
    'existence_test : EXISTS subquery'
    pass

def p_subquery(p):
    'subquery : LPAREN SELECT opt_all_distinct table_exp RPAREN '
    pass

def p_when_action(p):
    '''when_action : GOTO ID
                | CONTINUE'''
    pass

def p_empty(p):
    'empty :'
    pass

#===================================================================================================================
# Otras Definiciones

def p_func(p):
  'func : data_type ID LPAREN func_arg RPAREN LBLOCK block RBLOCK'
  pass

def p_func_arg(p):
  ''' func_arg : manipulative_statement
               | data_type ID
               | manipulative_statement COMMA func_arg
  ''' 

def p_if_statement(p):
  'if_statement : IF LPAREN comparison_predicate RPAREN LBLOCK block RBLOCK'

def p_foreach_statement(p):
  '''foreach_statement : FOREACH LPAREN comparison_predicate AS assignment RPAREN LBLOCK block RBLOCK
                       | FOREACH LPAREN comparison_predicate AS ID EQUAL manipulative_statement RPAREN LBLOCK block RBLOCK
                     '''

def p_block(p):
  ''' block : empty
            | block_recursiv
  '''

def p_block_recursiv(p):
  '''block_recursiv : sql_list
                    | while 
                    | print 
                    | if_statement
                    | foreach_statement
                    | block_recursiv block_recursiv'''
  pass

def p_comparison_simbol(p):
  ''' comparison_simbol : EQUAL
                        | DISTINT
                        | DIFF
                        | LESS
                        | GREATER
                        | LESSEQUAL
                        | GREATEREQUAL
                        | DEQUAL
                        | ISEQUAL
  '''
  pass

def p_while(p):
  'while : WHILE LPAREN comparison_predicate RPAREN LBLOCK block RBLOCK'

def p_print(p):
  'print : PRINT LPAREN atom RPAREN SEMICOLON'


#===================================================================================================================
#manejo de errores
def p_error(p):
    if p is not None:
        print "oe bebe en la linea " + str(p.lexer.lineno) + ", no me esperba esto: " + str(p.value)
    else:
        print "oiga bebe, hay un error sintactico en la linea " + str(lexxer.lexer.lineno)

#===================================================================================================================
# Prueba de Analizador

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.sql'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("\n Ya termine bebe, ahora que hacemos? \n ")
	#input()


