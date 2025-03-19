import sys
import ply.lex as lex
from ply.lex import TOKEN

# Definiciones de expresiones regulares auxiliares
digito = r'[0-9]'
numero = r'(' + digito + r')+'
letra = r'[a-zA-Z]'


# Lista de tokens. Siempre REQUERIDO
tokens = (
    "NUMERO",
    "HEXADECIMAL",
    "PALABRA_PYTHON",
    "IDENTIFICADOR_JAVA",
    "ESPACIO",
)


# Definición de reglas en una sóla línea sin acción léxica

# captar palabras reservadas de Python
t_PALABRA_PYTHON = r'(import|return|if|else|for)'
t_IDENTIFICADOR_JAVA = r'(?!return|if|for|else|import)[a-zA-Z_$][a-zA-Z0-9_$]{0,31}'
t_ESPACIO = r'[\s \t]+'


# Definición de reglas con acción léxica
@TOKEN(r'0[xX][0-9a-fA-F]+')
def t_HEXADECIMAL(t):
    print(f"Encontré un hexadecimal: {t.value} y su valor es {int(t.value, 16)}")
    return t

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

#t_ignore  = " \t" # Para aceptar espacios, comeentar esta linea

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
data = """
import tarea1
x
if x esIgual a 5
    return 5
else
    return 6
"""

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
