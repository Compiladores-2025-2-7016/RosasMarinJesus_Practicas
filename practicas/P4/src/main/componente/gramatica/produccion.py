from typing import List
from ..gramatica.simbolo import Simbolo


class Produccion:
    
    def __init__(self, cabeza: Simbolo = None, cuerpo: List[Simbolo] = None):
        self.cabeza = cabeza
        self.cuerpo = cuerpo if cuerpo is not None else []

    def __str__(self):
        """
        Representación en cadena de la producción.
        :return: Cadena que representa la producción.
        """
        cabeza_str = self.cabeza.sim.value
        cuerpo_str = ' '.join([sim.sim.value for sim in self.cuerpo]) if self.cuerpo else 'ε'
        return f"{cabeza_str} → {cuerpo_str}"
