import ply.lex as lex
from ply.lex import TOKEN
from componente.clase_lexica import ClaseLexica
from componente.componente_lexico import ComponenteLexico


class Lexer(object):
    """
    Analizador léxico para el lenguaje.
    Este lexer usa la librería PLY.
    """
    # Definiciones de expresiones regulares auxiliares
    digito = r'[0-9]'
    numero = r'(' + digito + r')+'
    letra = r'[a-zA-Z]'
    exponente = r'([eE][+-]?' + numero + r')'
    real = r'(' + digito + r'+\.' + digito + r'+(' + exponente + r')?)'

    # Identificador pero sin las palabras reservadas while, if, else, int, float
    identificador = r'(?!while\b|if\b|else\b|int\b|float\b)' + r'(' + letra + r'|_)([a-zA-Z0-9_]*)'

    # Número entero o real
    entero_o_real = r'(' + real + r'|' + numero + r')'

    # Lista de tokens. Siempre REQUERIDO
    tokens = list(ClaseLexica._member_names_) 

    # Definición de reglas con acción léxica
    
    @TOKEN(entero_o_real)
    def t_NUMERO(self, t):
        """
        Regla para reconocer un número entero o real.
        
        Parámetros:
        - t (LexToken): token que contiene el número.
        
        Retorna:
        LexToken: token con la clase y lexema correspondiente.
        """
        t.value = ComponenteLexico(ClaseLexica.NUMERO, t.value)
        return t
    
    
    @TOKEN(identificador)
    def t_ID(self, t):
        """
        Regla para reconocer un identificador.
        
        Parámetros:
        - t (LexToken): token que contiene el identificador.
        
        Retorna:
        LexToken: token con la clase y lexema correspondiente.
        """
        t.value = ComponenteLexico(ClaseLexica.ID, t.value)
        return t

    # Palabras reservadas
    def t_INT(self, t):
        r'int'
        """
        Regla para reconocer la palabra reservada 'int'.
        
        Parámetros:
        - t (LexToken): token que contiene la palabra reservada.
        
        Retorna:
        LexToken: token con la clase y lexema INT.
        """
        t.value = ComponenteLexico(ClaseLexica.INT, t.value)
        return t
    
    def t_FLOAT(self, t):
        r'float'
        """"
        Regla para reconocer la palabra reservada 'float'.

        Parámetros:
        - t (LexToken): token que contiene la palabra reservada.

        Retorna:
        LexToken: token con la clase y lexema FLOAT.
        """
        t.value = ComponenteLexico(ClaseLexica.FLOAT, t.value)
        return t
    
    def t_IF(self, t):
        r'if'
        """
        Regla para reconocer la palabra reservada 'if'.
        
        Parámetros:
        - t (LexToken): token que contiene la palabra reservada.
        
        Retorna:
        LexToken: token con la clase y lexema IF.
        """
        t.value = ComponenteLexico(ClaseLexica.IF, t.value)
        return t

    def t_ELSE(self, t):
        r'else'
        """
        Regla para reconocer la palabra reservada 'else'.
        
        Parámetros:
        - t (LexToken): token que contiene la palabra reservada.
        
        Retorna:
        LexToken: token con la clase y lexema ELSE.
        """
        t.value = ComponenteLexico(ClaseLexica.ELSE, t.value)
        return t
    
    def t_WHILE(self, t):
        r'while'
        """
        Regla para reconocer la palabra reservada 'while'.
        
        Parámetros:
        - t (LexToken): token que contiene la palabra reservada.
        
        Retorna:
        LexToken: token con la clase y lexema WHILE.
        """
        t.value = ComponenteLexico(ClaseLexica.WHILE, t.value)
        return t

    # Simbolos
    def t_PYC(self, t):
        r';'
        """
        Regla para reconocer el punto y coma (;).
        
        Parámetros:
        - t (LexToken): token que contiene el punto y coma.
        
        Retorna:
        LexToken: token con la clase y lexema PYC.
        """
        # Usamos constructor sin lexema
        t.value = ComponenteLexico(ClaseLexica.PYC)
        return t
    
    def t_COMA(self, t):
        r','
        """
        Regla para reconocer la coma (,).
        
        Parámetros:
        - t (LexToken): token que contiene la coma.
        
        Retorna:
        LexToken: token con la clase y lexema COMA.
        """
        # Usamos constructor sin lexema
        t.value = ComponenteLexico(ClaseLexica.COMA)
        return t
    
    def t_LPAR(self, t):
        r'\('
        """
        Regla para reconocer el paréntesis izquierdo (.
        
        Parámetros:
        - t (LexToken): token que contiene el paréntesis izquierdo.
        
        Retorna:
        LexToken: token con la clase y lexema LPAR.
        """
        # Usamos constructor sin lexema
        t.value = ComponenteLexico(ClaseLexica.LPAR)
        return t
    
    def t_RPAR(self, t):
        r'\)'
        """
        Regla para reconocer el paréntesis derecho ).

        Parámetros:
        - t (LexToken): token que contiene el paréntesis derecho.

        Retorna:
        LexToken: token con la clase y lexema RPAR.
        """
        # Usamos constructor sin lexema
        t.value = ComponenteLexico(ClaseLexica.RPAR)
        return t

    # Definimos una regla para el manejo de número de líneas
    def t_newline(self, t):
        r'\n+' # docstring contiene la regex que maneja el salto de línea
        """
        Regla para manejar el número de líneas.
        
        Parámetros:
        - t (LexToken): token que contiene el salto de línea.
        """
        t.lexer.lineno += len(t.value) # Aumentamos la variable de número de línea del Analizador

    # Una cadena que contiene todos los caracteres que deben ignorarse
    # ej. Espacios y tabuladores
    t_ignore  = " \t"


    # Esta función nos permite manejar el estado de error a nuestra conveniencia
    def t_error(self, t):
        """
        Función para manejar los errores léxicos.

        Parámetros:
        - t (LexToken): token que contiene
        """
        print("Error léxico. Caracter no reconocido: '%s'" % t.value[0])
        t.lexer.skip(1)

    # Función que nos permite construir el analizador léxico
    # NO TOCAR
    def build(self, **kwargs):
        """
        Construye el analizador léxico.
        
        Parámetros:
        - kwargs: argumentos adicionales.
        """
        self.lexer = lex.lex(module=self, **kwargs)


    # Función que nos permite efectuar un análisis léxico
    # sobre una entrada
    def scan(self, data):
        """
        Realiza el análisis léxico sobre una entrada.
        
        Parámetros:
        - data (str): cadena de texto a analizar.
        
        Retorna:
        list<ComponenteLexico>: lista de componentes léxicos.
        """
        self.lexer.input(data)
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok: 
               break
            tokens.append(tok.value)
        return tokens