from componente.clase_lexica import ClaseLexica

class ComponenteLexico(): # también llamado token
    """
    Clase que representa un componente léxico (token).
    
    Atributos:
    - clase (ClaseLexica): clase léxica asociada al componente léxico.
    - lexema (str): lexema asociado al componente léxico. Sí es None, el componente
      léxico no tiene lexema.
    """

    def __init__(self, clase, lexema=None):
        """
        Constructor de la clase ComponenteLexico.

        Parámetros:
        - clase (ClaseLexica): clase léxica asociada al componente léxico.
        - lexema (str): lexema asociado al componente léxico. Por defecto es None.
        """
        self.clase = clase
        self.lexema = lexema


    def __str__(self):
        """
        Método que devuelve una representación en cadena del componente léxico.

        Retorna:
        str: Representación en cadena del componente léxico.
        """
        if self.lexema is None: # Si no  tiene lexema
            return f"<{self.clase.name}>"
        else:
            return f"<{self.clase.name}, {self.lexema}>"