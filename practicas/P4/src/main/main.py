from analisis.sintactico import ParserLL
from analisis.lexico import Lexer

data = """42+2"""

scanner = Lexer()
scanner.build()
#scanner.scan("3 y 4")
scanner.lexer.input(data)

parser = ParserLL(scanner)
parser.parse()
