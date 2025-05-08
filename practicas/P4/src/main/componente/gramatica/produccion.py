from typing import List
from ..gramatica.simbolo import Simbolo


class Produccion:
    
    def __init__(self, cabeza: Simbolo = None, cuerpo: List[Simbolo] = None):
        self.cabeza = cabeza
        self.cuerpo = cuerpo if cuerpo is not None else []

    