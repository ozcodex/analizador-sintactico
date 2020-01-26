# ==================================================================================================================
#  lexxer_v3.py                                                                                   
#  Analizador Lexico - Compilador en Phyton para SQL92                                                                            
#  Construido por:
#                       Kenny Bedoya        1088305866
#						Oscar Bernal        1088304958
#                       Sebastian Zapata    1088302207
#===================================================================================================================
import ply.lex as lex
import sys
#===================================================================================================================
# Declaracion de Tokens

tokens=[
# Palabras Reservadas SQL92 SQL93

	'CREATE','CASE','COALESCE','CROSS','CURRENT','CURRENT_USER','DEC','DECIMAL','ELSE',
	'ENDFALSE','FOREIGN','GLOBAL','GROUP','LOCALNULLIF','NUMERIC','ORDER','POSITION',
	'PRECISION','SESSION_USER','TABLE','THEN','TRANSACTION','TRUEUSER','WHENADD','ALL',
	'ALTER','AND','ANY','AS','ASCBEGIN','BETWEEN','BOTH','BYCASCADE','CAST','CHAR',
	'CHARACTER','CHECK','CLOSECOLLATE','COLUMN','COMMIT','CONSTRAINT','CREATECURRENT_DATE',
	'CURRENT_TIME','CURRENT_TIMESTAMP','CURSORDECLARE','DEFAULT','DELETE','DISTINCT',
	'DROPEXECUTE','EXISTS','EXTRACTFETCH','FOR','FROM','FULLGRANT','HAVINGIN','INNER',
	'INSERT','INTO','ISJOIN','LEADING','LEFT','LIKE','LOCALNAMES','NATIONAL','NATURAL',
	'NCHAR','NOT','NULL','ON','OR','OUTERPARTIAL','PRIMARY','PRIVILEGES','PROCEDURE',
	'PUBLICREFERENCES','REVOKE','RIGHT','ROLLBACKSELECT','SET','SUBSTRINGTO','TRAILING',
	'TRIM','UNION','UNIQUE','UPDATE','USINGVALUES','VARCHAR','VARYING','VIEWWHERE','WITH',
	'WORK',
	#'DESC',
#-------------------------------------------------------------------------------------------------------------------
# Tipos
	'BOOLEAN','DOUBLE','FLOAT','INT','INTEGER','INTERVAL','REAL','SMALLINT',
#-------------------------------------------------------------------------------------------------------------------
# Simbolos
	'PLUS','MINUS','TIMES','DIVIDE','EQUAL','DISTINT','LESS','GREATER','SEMICOLON','COMMA',
	'LPAREN','RPAREN','LBRACKET','RBRACKET','LBLOCK','RBLOCK','COLON','AMPERSANT','HASHTAG',
	'DOT',
#-------------------------------------------------------------------------------------------------------------------
# Numero e ID
	'NUMBER','ID',
#-------------------------------------------------------------------------------------------------------------------
# Especiales
	'LESSEQUAL','GREATEREQUAL','DEQUAL','ISEQUAL','MIN','MAX',
#-------------------------------------------------------------------------------------------------------------------
# Otros
	'WHENEVER','FOUND','SQLERROR','SCHEMA','AUTHORIZATION','DATE','IDENTITY','BIT',
	'SMALLDATETIME','KEY','USER','REFERENCES','VIEW','OPTION','GRANT','TO','SELECT',
	'PUBLIC','DECLARE','CURSOR','BY','ASC','OPEN','CLOSE','ROLLBACK','WHERE','OF',
	'FETCH','INDICATOR','INDICADOR','VALUES','APOSTROPHE','HAVING','COMPARISON','ESCAPE',
	'IS','IN','SOME','GOTO','CONTINUE','DROP','WHILE','PRINT','TRIGGER','DIFF','DOSCOMILLAS',
	'IF','FOREACH'
]
#===================================================================================================================
# Definiciones de Simbolos

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_DISTINT = r'<>'
t_DIFF = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_SEMICOLON = r';'
t_COMMA = r','
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COLON = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_DOSCOMILLAS = r'\"'

#===================================================================================================================
# Definiciones de Palabras Reservadas

def t_CREATE(t):
	r'create'
	return t

def t_CASE(t):
	r'case'
	return t

def t_COALESCE(t):
	r'coalesce'
	return t

def t_CROSS(t):
	r'cross'
	return t

def t_CURRENT(t):
	r'current'
	return t

def t_CURRENT_USER(t):
	r'current_user'
	return t

def t_DEC(t):
	r'dec'
	return t

def t_DECIMAL(t):
	r'decimal'
	return t

def t_ELSE(t):
	r'else'
	return t

def t_ENDFALSE(t):
	r'endfalse'
	return t

def t_FOREIGN(t):
	r'foreign'
	return t

def t_GLOBAL(t):
	r'global'
	return t

def t_GROUP(t):
	r'group'
	return t

def t_LOCALNULLIF(t):
	r'localnullif'
	return t

def t_NUMERIC(t):
	r'numeric'
	return t

def t_ORDER(t):
	r'order'
	return t

def t_POSITION(t):
	r'position'
	return t

def t_PRECISION(t):
	r'precision'
	return t

def t_SESSION_USER(t):
	r'session_user'
	return t

def t_TABLE(t):
	r'table'
	return t

def t_THEN(t):
	r'then'
	return t

def t_TRANSACTION(t):
	r'transaction'
	return t

def t_TRUEUSER(t):
	r'trueuser'
	return t

def t_WHENADD(t):
	r'whenadd'
	return t

def t_ALL(t):
	r'all'
	return t

def t_ALTER(t):
	r'alter'
	return t

def t_AND(t):
	r'and'
	return t

def t_ANY(t):
	r'any'
	return t

def t_AS(t):
	r'as'
	return t

def t_ASCBEGIN(t):
	r'ascbegin'
	return t

def t_BETWEEN(t):
	r'between'
	return t

def t_BOTH(t):
	r'both'
	return t

def t_BYCASCADE(t):
	r'bycascade'
	return t

def t_CAST(t):
	r'cast'
	return t

def t_CHAR(t):
	r'char'
	return t

def t_CHARACTER(t):
	r'character'
	return t

def t_CHECK(t):
	r'check'
	return t

def t_CLOSECOLLATE(t):
	r'closecollate'
	return t

def t_COLUMN(t):
	r'column'
	return t

def t_COMMIT(t):
	r'commit'
	return t

def t_CONSTRAINT(t):
	r'constraint'
	return t

def t_CREATECURRENT_DATE(t):
	r'createcurrent_date'
	return t

def t_CURRENT_TIME(t):
	r'current_time'
	return t

def t_CURRENT_TIMESTAMP(t):
	r'current_timestamp'
	return t

def t_CURSORDECLARE(t):
	r'cursordeclare'
	return t

def t_DEFAULT(t):
	r'default'
	return t

def t_DELETE(t):
	r'delete'
	return t

#def t_DESC(t):
#	r'desc'
#	return t

def t_DISTINCT(t):
	r'distinct'
	return t

def t_DROPEXECUTE(t):
	r'dropexecute'
	return t

def t_EXISTS(t):
	r'exists'
	return t

def t_EXTRACTFETCH(t):
	r'extractfetch'
	return t

def t_FOREACH(t):
	r'foreach'
	return t

def t_FOR(t):
	r'for'
	return t

def t_FROM(t):
	r'from'
	return t

def t_FULLGRANT(t):
	r'fullgrant'
	return t

def t_HAVINGIN(t):
	r'havingin'
	return t

def t_INNER(t):
	r'inner'
	return t

def t_INSERT(t):
	r'insert'
	return t

def t_INTO(t):
	r'into'
	return t

def t_ISJOIN(t):
	r'isjoin'
	return t

def t_LEADING(t):
	r'leading'
	return t

def t_LEFT(t):
	r'left'
	return t

def t_LIKE(t):
	r'like'
	return t

def t_LOCALNAMES(t):
	r'localnames'
	return t

def t_NATIONAL(t):
	r'national'
	return t

def t_NATURAL(t):
	r'natural'
	return t

def t_NCHAR(t):
	r'nchar'
	return t

def t_NOT(t):
	r'not'
	return t

def t_NULL(t):
	r'null'
	return t

def t_ON(t):
	r'on'
	return t

def t_OR(t):
	r'or'
	return t

def t_OUTERPARTIAL(t):
	r'outerpartial'
	return t

def t_PRIMARY(t):
	r'primary'
	return t

def t_PRIVILEGES(t):
	r'privileges'
	return t

def t_PROCEDURE(t):
	r'procedure'
	return t

def t_PUBLICREFERENCES(t):
	r'publicreferences'
	return t

def t_REVOKE(t):
	r'revoke'
	return t

def t_RIGHT(t):
	r'right'
	return t

def t_ROLLBACKSELECT(t):
	r'rollbackselect'
	return t

def t_SET(t):
	r'set'
	return t

def t_SUBSTRINGTO(t):
	r'substringto'
	return t

def t_TRAILING(t):
	r'trailing'
	return t

def t_TRIM(t):
	r'trim'
	return t

def t_UNION(t):
	r'union'
	return t

def t_UNIQUE(t):
	r'unique'
	return t

def t_UPDATE(t):
	r'update'
	return t

def t_USINGVALUES(t):
	r'usingvalues'
	return t

def t_VARCHAR(t):
	r'varchar'
	return t

def t_VARYING(t):
	r'varying'
	return t

def t_VIEWWHERE(t):
	r'viewwhere'
	return t

def t_WITH(t):
	r'with'
	return t

def t_WORK(t):
	r'work'
	return t

#-------------------------------------------------------------------------------------------------------------------
# Definiciones de Tipos

def t_BOOLEAN(t):
	r'boolean'
	return t

def t_DOUBLE(t):
	r'double'
	return t

def t_FLOAT(t):
	r'float'
	return t

def t_INT(t):
	r'int'
	return t

def t_INTEGER(t):
	r'integer'
	return t

def t_INTERVAL(t):
	r'interval'
	return t

def t_REAL(t):
	r'real'
	return t

def t_SMALLINT(t):
	r'smallint'
	return t	
#===================================================================================================================
# Definicion de Numeros 
def t_NUMBER(t):
	#r'\d+(\.\d+)?'
	r'(((-)?\d+(\.\d+)?)(E|e(-)?\d+)?)'
	#t.value = float(t.value)
	return t
#-------------------------------------------------------------------------------------------------------------------
# Definiciones especiales de simbolos

def t_LESSEQUAL(t):
	r'<='
	return t

def t_GREATEREQUAL(t):
	r'>='
	return t

def t_DEQUAL(t):
	r'<>'
	return t

def t_ISEQUAL(t):
	r'=='
	return t

def t_MIN(t):
	r'min'
	return t

def t_MAX(t):
	r'max'
	return t

#-------------------------------------------------------------------------------------------------------------------
# Definicion de Comentarios

def t_comments(t):
	r'--(.)*?\n'
	t.lexer.lineno += 1
	print "comentario: "+t.value,#

"""
def t_longcomments(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')
	print ("se ha detectado un comentario largo"))
"""

#-------------------------------------------------------------------------------------------------------------------
# Definicion de nueva linea

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore = ' \t\r'

#-------------------------------------------------------------------------------------------------------------------
# Otras Definiciones

def t_WHENEVER(t):
	r'whenever'
	return t

def t_FOUND(t):
	r'found'
	return t
	
def t_SQLERROR(t):
	r'sqlerror'
	return t
	
def t_SCHEMA(t):
	r'schema'
	return t
	
def t_AUTHORIZATION(t):
	r'authorization'
	return t
	
def t_DATE(t):
	r'date'
	return t
	
def t_IDENTITY(t):
	r'identity'
	return t
	
def t_BIT(t):
	r'bit'
	return t
	
def t_SMALLDATETIME(t):
	r'smalldatetime'
	return t
	
def t_KEY(t):
	r'key'
	return t
	
def t_USER(t):
	r'user'
	return t
	
def t_REFERENCES(t):
	r'references'
	return t
	
def t_VIEW(t):
	r'view'
	return t
	
def t_OPTION(t):
	r'option'
	return t
	
def t_GRANT(t):
	r'grant'
	return t
	
def t_TO(t):
	r'to'
	return t
	
def t_SELECT(t):
	r'select'
	return t
	
def t_PUBLIC(t):
	r'public'
	return t
	
def t_DECLARE(t):
	r'declare'
	return t
	
def t_CURSOR(t):
	r'cursor'
	return t
		
def t_ASC(t):
	r'asc'
	return t
	
def t_OPEN(t):
	r'open'
	return t
	
def t_CLOSE(t):
	r'close'
	return t
	
def t_ROLLBACK(t):
	r'rollback'
	return t
	
def t_WHERE(t):
	r'where'
	return t
	
def t_OF(t):
	r'of'
	return t
	
def t_FETCH(t):
	r'fetch'
	return t
	
def t_INDICATOR(t):
	r'indicator'
	return t

def t_INDICADOR(t):
	r'indicador'
	return t

def t_VALUES(t):
	r'values'
	return t
	
def t_APOSTROPHE(t):
	r'\''
	return t
	
def t_BY(t):
	r'by'
	return t
	
def t_HAVING(t):
	r'having'
	return t
	
def t_COMPARISON(t):
	r'comparison'
	return t
	
def t_ESCAPE(t):
	r'escape'
	return t
	
def t_IS(t):
	r'is'
	return t
	
def t_IN(t):
	r'in'
	return t
	
def t_SOME(t):
	r'some'
	return t
	
def t_GOTO(t):
	r'goto'
	return t
	
def t_CONTINUE(t):
	r'continue'
	return t
	
def t_DROP(t):
	r'drop'
	return t

def t_WHILE(t):
	r'while'
	return t

def t_PRINT(t):
	r'print'
	return t

def t_TRIGGER(t):
	r'trigger'
	return t

def t_IF(t):
	r'if'
	return t

#-------------------------------------------------------------------------------------------------------------------
# Definiciones de identificador

def t_ID(t):
	#r'(\$[^aeiouAEIOU_\d\W]\w*)'
	r'\w+(_\d\w)*'
	if t.value.upper() in tokens:
		t.type = t.value.upper()
        return t
	return t

#-------------------------------------------------------------------------------------------------------------------
# Definicion Error

def t_error(t):
	print ("Baby, hay error lexico con: \"" + str(t.value[0]) +"\" en la linea "+ str(t.lexer.lineno))
	t.lexer.skip(1)

#-------------------------------------------------------------------------------------------------------------------
# Test de tokens

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)	

#===================================================================================================================
#------MAIN---------

lexer = lex.lex()
 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.sql'
	f = open(fin, 'r')
	data = f.read()
	#print (data)
	lexer.input(data)
	test(data, lexer)
	#input()
# ==================================================================================================================
#  lexxer                                                                                   
#  Analizador Lexico - Compilador en Phyton para SQL92                                                                            
#  Modificado por:
#                       Kenny Bedoya        1088305866
#						Oscar Bernal        1088304958
#                       Sebastian Zapata    1088302207
#===================================================================================================================
