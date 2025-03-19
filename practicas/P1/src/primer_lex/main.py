import sys
import ply.lex as lex
from ply.lex import TOKEN

# Definiciones de expresiones regulares auxiliares
digito = r'[0-9]'
numero = r'(' + digito + r')+'
letra = r'[a-zA-Z]'


# Lista de tokens. Siempre REQUERIDO
tokens = (
    "PALABRA",
    "NUMERO",
    "PARIZQ",
    "PARDER",
    #"ESPACIO", # Para aceptar espacios, descomentar esta línea
)


# Definición de reglas en una sóla línea sin acción léxica
t_PALABRA = r'(' + letra + r'+)'
t_PARIZQ = r'\('
t_PARDER = r'\)'
#t_ESPACIO = r'\ +' # Para aceptar espacios, descomentar esta línea
 

# Definición de reglas con acción léxica
#@TOKEN(numero)
@TOKEN(r'(' + digito + r')+')
def t_NUMERO(t):
    print("Encontré un número:", t.value)
    return t


# Definimos una regla para el manejo de número de líneas
def t_newline(t):
    r'\n+' # docstring contiene la regex que maneja el salto de línea
    t.lexer.lineno += len(t.value) # Aumentamos la variable de número de línea del Analizador


# Una cadena que contiene todos los caracteres que deben ignorarse
# ej. Espacios y tabuladores

t_ignore  = " \t" # Para aceptar espacios, comeentar esta linea

# Calcula la posición de la columna en la línea actual
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start)+ 1

# Esta función nos permite manejar el estado de error a nuestra conveniencia
def t_error(t):
    col = find_column(t.lexer.lexdata, t)
    print("Error léxico. Caracter no reconocido: '%s'" % t.value[0] +
           " en la línea " + str(t.lineno) + ", columna " + str(col))
    t.lexer.skip(1)




###### Instanciación y uso del Analizador Léxico ######

# Construcción del Scanner
lexer = lex.lex()


# Código fuente
data = '''
Hola mundo 
La respuesta es 42
'''

# En caso de que estemos leyendo un archivo señalado desde la línea de argumentos
if (len(sys.argv) > 1):
    with open(sys.argv[1], 'r') as file:
        data = file.read()

lexer.input(data)

# Tokenización
while True:
    tok = lexer.token()
    if not tok: 
        break      # Termina el análisis
    print(tok)
