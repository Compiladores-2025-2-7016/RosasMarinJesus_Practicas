import sys
from analisis.sintactico import ParserLL
from analisis.lexico import Lexer

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_del_archivo>")
        sys.exit(1)

    ruta_archivo = sys.argv[1]

    try:
        with open(ruta_archivo, 'r') as archivo:
            data = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
        sys.exit(1)
    # data = """42+2"""

    scanner = Lexer()
    scanner.build()
    #scanner.scan("3 y 4")
    scanner.lexer.input(data)

    parser = ParserLL(scanner)
    parser.parse() 