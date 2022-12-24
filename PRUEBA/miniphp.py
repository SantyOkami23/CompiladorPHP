#Se importan las librerias
import ply.lex as lex
import sys

#creacion de los tokens
tokens = (
    # Reserverd words
    "PUBLIC",
    "PROTECTED",
    "PRIVATE",
    "CLASS",
    "PHP",
    "FUNCTION",
    "ECHO",
    "NEW",
    "IF",
    "EXTENDS",
    "FOR",

    # Symbols
    "PLUS", #+
    "MINUS", #-
    "TIMES", #*
    "DIVIDE",# /
    "ASSIGN", # =
    "LPAREN", #(
    "RPAREN", #)
    "LESS",  #<
    "GREATER", #> 
    "LBLOCK", #{
    "RBLOCK", #}
    "COMMA", #,
    "SEMICOLON", #;
    "DOLLAR", #$
    "PREG", #?
    "PORCENT", # %
    "COMILLASIMPLE", #'
    "JUMP",
    "COMMENT",

    # Others 
    "ID",
    "NUMBER"
)

#expresiones regulares para los simbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LESS = r'<'
t_GREATER = r'>'
t_LBLOCK = r'{'
t_RBLOCK = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_DOLLAR = r'\$'
t_PREG  = r'\?'
t_PORCENT = r'%'
t_COMILLASIMPLE = r'\''
t_JUMP = r'\n'

#palabras reservadas
def t_PUBLIC(t):
    r'public'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_PHP(t):
    r'php'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_NEW(t):
    r'new'
    return t

def t_IF(t):
    r'if'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FOR(t):
    r'for'
    return t



t_ignore = '  \t'

def t_ID(t):
    r'(\$[a-zA-Z_](_|[a-zA-Z0-9])*)|[a-zA-Z_](_|[a-zA-Z0-9])*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_COMMENT(t):
    r'(\/\/.*)|(\/\*.*\*\/)'
    return t

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
            print (tok)
            lexer = lex.lex()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fin: str= sys.argv[1]
    else:
        fin = 'nombreDocumento.txt'
        f = open(fin, 'r')
        data = f.read()
        print (data)
        lexer.input(data)
        test(data,lexer)
    print("Amiguito, tengo el placer de informar que Tu parser reconocio correctamente todo")
#input()



