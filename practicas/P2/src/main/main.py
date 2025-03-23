import sys
from lexer.scanner import Lexer

# Ejecución prueba

#lexer = Lexer()
#lexer.build()
#lexer.scan("3 y 4")

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.

    Este script realiza el análisis léxico de un archivo de entrada..
    El archivo de entrada se especifica como un argumento en la línea de comandos.

    Uso:
        python main.py <ruta_del_archivo>

    Args:
        sys.argv[1] (str): Ruta del archivo de entrada a analizar.

    Raises:
        FileNotFoundError: Si el archivo de entrada no se encuentra.
    """
    # Verificamos que el usuario proporcione un archivo de entrada
    if len(sys.argv) < 2:
        print("Uso: python main.py <ruta_del_archivo>")
        sys.exit(1)
    
    archivo_entrada = sys.argv[1]
    
    try:
        with open(archivo_entrada, 'r') as archivo:
            contenido = archivo.read()  # Leer el contenido del archivo
    except FileNotFoundError:
        print(f"El archivo {archivo_entrada} no se encontró.")
        sys.exit(1)
    
    # Instanciamos el lexer
    lexer = Lexer()

    # Construimos el lexer
    lexer.build()

    # Realizamos el análisis léxico
    tokens = lexer.scan(contenido)  # Pasamos el contenido del archivo al lexer

    # Imprimimos los tokens
    for token in tokens:
        print(token)