from analisis.lexico import Lexer
from componente.clase_lexica import ClaseLexica

class Parser:

    def __init__(self, lexer: Lexer):
        self.an_lexico = lexer
        self.token_actual = 0


    def eat(self, clase_lexica: int):
        if self.token_actual == clase_lexica:
            try:
                tok = self.an_lexico.lexer.token()
                if not tok: # No hay mas entrada
                    self.token_actual = 0
                else:
                    self.token_actual = ClaseLexica[tok.type].value
            except Exception as e:
                print("No fue posible leer el siguiente token. {excp}".format(excp=str(e)))
        else:
            print("Se esperaba el token: {actual}".format(actual=self.token_actual))


    def error(self, msg: str):
        print("ERROR DE SINTAXIS: {mensaje}. En la línea {linea}".format(mensaje=msg, 
                                                                         linea=self.an_lexico.lexer.lineno))

    def parse(self):
        try:
            tok = self.an_lexico.lexer.token()
            self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print("No fue posible obtener el primer token de la entrada: {excepcion}".format(excepcion=str(e)))
            exit(1)

        self.S()
        if self.token_actual == 0: # llegamos al EOF sin error
            print("La cadena es aceptada")
        else:
            print("La cadena no pertenece al lenguaje generado por la gramática")


    # Conjunto P

    """"
        programa → declaraciones sentencias
        declaraciones → declaracion declaraciones'
        declaraciones' → declaracion declaraciones' | ε
        declaracion → tipo lista_var ;
        tipo → int | float
        lista_var → identificador lista_var'
        lista_var' → , identificador lista_var' | ε
        sentencias → sentencia sentencias'
        sentencias' → sentencia sentencias' | ε
        sentencia → identificador = expresion ; | if ( expresion ) sentencias else sentencias | while ( expresion ) sentencias
        expresion → expresion_mult expresion'
        expresion' → + expresion_mult expresion' | - expresion_mult expresion' | ε
        expresion_mult → expresion_unaria expresion_mult'
        expresion_mult' → * expresion_unaria expresion_mult' | / expresion_unaria expresion_mult' | ε
        expresion_unaria → ( expresion ) | identificador | numero
    """

    
    def S(self):
        """S (programa) → declaraciones sentencias"""
        self.declaraciones()
        self.sentencias()

    def declaraciones(self):
        """declaraciones → declaracion declaraciones'"""
        self.declaracion()
        self.declaraciones_p()

    def declaraciones_p(self):
        """declaraciones' → declaracion declaraciones' | ε"""
        if self.token_actual in [ClaseLexica.INT.value, ClaseLexica.FLOAT.value]:
            self.declaracion()
            self.declaraciones_p()

    def declaracion(self):
        """declaracion → tipo lista_var ;"""
        self.tipo()
        self.lista_var()
        self.eat(ClaseLexica.PYC.value)

    def tipo(self):
        """tipo → int | float"""
        if self.token_actual == ClaseLexica.INT.value:
            self.eat(ClaseLexica.INT.value)
        elif self.token_actual == ClaseLexica.FLOAT.value:
            self.eat(ClaseLexica.FLOAT.value)
        else:
            self.error("Se esperaba 'int' o 'float'")

    def lista_var(self):
        """lista_var → identificador lista_var'"""
        self.eat(ClaseLexica.ID.value)
        self.lista_var_p()

    def lista_var_p(self):
        """lista_var' → , identificador lista_var' | ε"""
        if self.token_actual == ClaseLexica.COMA.value:
            self.eat(ClaseLexica.COMA.value)
            self.eat(ClaseLexica.ID.value)
            self.lista_var_p()

    def sentencias(self):
        """sentencias → sentencia sentencias'"""
        self.sentencia()
        self.sentencias_p()

    def sentencias_p(self):
        """sentencias' → sentencia sentencias' | ε"""
        if self.token_actual in [ClaseLexica.ID.value, ClaseLexica.IF.value, ClaseLexica.WHILE.value]:
            self.sentencia()
            self.sentencias_p()

    def sentencia(self):
        """sentencia → identificador = expresion ;"""
        if self.token_actual == ClaseLexica.ID.value:
            self.eat(ClaseLexica.ID.value)
            self.eat(ClaseLexica.IGUAL.value)
            self.expresion()
            self.eat(ClaseLexica.PYC.value)

        elif self.token_actual == ClaseLexica.IF.value:
            self.eat(ClaseLexica.IF.value)
            self.eat(ClaseLexica.LPAR.value)
            self.expresion()
            self.eat(ClaseLexica.RPAR.value)
            self.sentencias()
            self.eat(ClaseLexica.ELSE.value)
            self.sentencias()

        elif self.token_actual == ClaseLexica.WHILE.value:
            self.eat(ClaseLexica.WHILE.value)
            self.eat(ClaseLexica.LPAR.value)
            self.expresion()
            self.eat(ClaseLexica.RPAR.value)
            self.sentencias()

        else:
            self.error("Se esperaba una sentencia de asignación, if o while")

    def expresion(self):
        """expresion → expresion_mult expresion'"""
        self.expresion_mult()
        self.expresion_p()

    def expresion_p(self):
        """expresion' → + expresion_mult expresion' | - expresion_mult expresion' | ε"""
        if self.token_actual == ClaseLexica.SUMA.value:
            self.eat(ClaseLexica.SUMA.value)
            self.expresion_mult()
            self.expresion_p()
        elif self.token_actual == ClaseLexica.RESTA.value:
            self.eat(ClaseLexica.RESTA.value)
            self.expresion_mult()
            self.expresion_p()

    def expresion_mult(self):
        """expresion_mult → expresion_unaria expresion_mult'"""
        self.expresion_unaria()
        self.expresion_mult_p()

    def expresion_mult_p(self):
        """expresion_mult' → * expresion_unaria expresion_mult' | / expresion_unaria expresion_mult' | ε"""
        if self.token_actual == ClaseLexica.MULT.value:
            self.eat(ClaseLexica.MULT.value)
            self.expresion_unaria()
            self.expresion_mult_p()
        elif self.token_actual == ClaseLexica.DIV.value:
            self.eat(ClaseLexica.DIV.value)
            self.expresion_unaria()
            self.expresion_mult_p()

    def expresion_unaria(self):
        """expresion_unaria → ( expresion ) | identificador | numero"""
        if self.token_actual == ClaseLexica.LPAR.value:
            self.eat(ClaseLexica.LPAR.value)
            self.expresion()
            self.eat(ClaseLexica.RPAR.value)
        elif self.token_actual == ClaseLexica.ID.value:
            self.eat(ClaseLexica.ID.value)
        elif self.token_actual == ClaseLexica.NUMERO.value:
            self.eat(ClaseLexica.NUMERO.value)
        else:
            self.error("Se esperaba un identificador, un número o una expresión entre paréntesis")