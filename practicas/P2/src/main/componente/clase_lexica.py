from enum import Enum

class ClaseLexica(Enum):
    """
    Enumeración que representa las clases léxicas de los componentes léxicos (tokens).
    
    Atributos:
    - INT (int): palabra reservada 'int'.
    - FLOAT (int): palabra reservada 'float'.
    - IF (int): palabra reservada 'if'.
    - ELSE (int): palabra reservada 'else'.
    - WHILE (int): palabra reservada 'while'.
    - NUMERO (int): número.
    - ID (int): identificador.
    - PYC (int): punto y coma.
    - COMA (int): coma.
    - LPAR (int): paréntesis izquierdo.
    - RPAR (int): paréntesis derecho.
    """
    INT = 1
    FLOAT = 2
    IF = 3
    ELSE = 4
    WHILE = 5
    NUMERO = 6
    ID = 7
    PYC = 8       # Punto y coma
    COMA = 9      # Coma
    LPAR = 10     # Paréntesis izquierdo
    RPAR = 11     # Paréntesis derecho