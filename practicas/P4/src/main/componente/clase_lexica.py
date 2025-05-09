from enum import Enum, auto

class ClaseLexica(Enum): #Estos serán miembro de alguna coordenada en la tabla LL(1)
    """
    Enumeración de las clases léxicas.
    """
    EOF = 0
    ESPACIO = 5
    # TODO: agregar las clases léxicas restantes
    NUMERO = 1 
    PLUS = 2


class NoTerminal(Enum): #Estos serán miembro de alguna coordenada en la tabla LL(1)
    """
    Enumeración de los no terminales de la gramática.
    """
    EPSILON = auto()
    # TODO: agregar los no terminales restantes
    S = auto()
    SPRIM = auto()