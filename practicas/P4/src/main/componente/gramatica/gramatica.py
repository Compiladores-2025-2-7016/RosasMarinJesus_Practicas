from typing import List, Dict

from ..gramatica.produccion import Produccion
from ..gramatica.simbolo import Simbolo
from enum import Enum  # para usar como tipo en el diccionario

class Gramatica:
    def __init__(self):
        self.simbolos: List[Simbolo] = []
        self.producciones: List[Produccion] = []
        self.simbolos_dict: Dict[Enum, Simbolo] = {}  # NUEVO: para acceso rápido

    def add_sim(self, simbolo: Simbolo):
        if simbolo.sim not in self.simbolos_dict:  # evitar duplicados
            self.simbolos.append(simbolo)
            self.simbolos_dict[simbolo.sim] = simbolo

    def add_prod(self, produccion: Produccion):
        self.producciones.append(produccion)

    def get_sim(self, clave: Enum) -> Simbolo:
        if clave in self.simbolos_dict:
            return self.simbolos_dict[clave]
        raise Exception(f"No existe un símbolo en la gramática con ese valor: {clave}")

    def get_prod(self, idx: int) -> Produccion:
        return self.producciones[idx]

    
