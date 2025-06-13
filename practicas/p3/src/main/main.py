from analisis.sintactico import Parser
from analisis.lexico import Lexer
import sys

#data = """42"""

# Cuando se ejecuta el script, se espera que reciba un archivo como argumento
if __name__ =="__main__":
    if len(sys.argv) == 2:
        with open(sys.argv[1],"r") as file:
           data = file.read() # Lee el contenido del archivo

# Lexer
# Instancia el analizador léxico 
scanner = Lexer()
scanner.build()
#scanner.scan("3 y 4")
scanner.lexer.input(data)
# Realiza el análisis léxico
parser = Parser(scanner)
# Instancia el analizador sintáctico
parser.parse() # Realiza el análisis sintáctico
