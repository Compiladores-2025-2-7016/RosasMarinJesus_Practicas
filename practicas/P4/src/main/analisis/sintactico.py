from typing import Dict, List
from analisis.lexico import Lexer
from componente.gramatica.produccion import Produccion
from componente.gramatica.simbolo import Simbolo
from componente.clase_lexica import ClaseLexica, NoTerminal
from componente.gramatica.gramatica import Gramatica


class ParserLL:

    def __init__(self, lexer: Lexer):
        self.an_lexico = lexer
        self.token_actual = 0
        self.gramatica = Gramatica()
        self.tabla: Dict[Simbolo, Dict[Simbolo, Produccion]] = {} # self.tabla[S_inicial][NUMERO] -> Produccion

    def eat(self):
        # hint: ip++ == self.eat()
        try:
            tok = self.an_lexico.lexer.token()
            if not tok: # No hay mas entrada
                self.token_actual = 0
            else:
                self.token_actual = ClaseLexica[tok.type].value
        except Exception as e:
            print("No fue posible leer el siguiente token. {excp}".format(excp=str(e)))


    def error(self, msg: str):
        print("ERROR DE SINTAXIS: {mensaje}. En la línea {linea}".format(mensaje=msg, 
                                                                         linea=self.an_lexico.lexer.lineno))
        exit(1)



    ########################################################################
    ##                                                                    ##
    ##                    TODO: Hardcodeo de la gramática                 ##
    ##                                                                    ##
    ########################################################################

    def load_syms(self):
        # TODO: Llenar la lista de símbolos de G.
        # hint: self.gramatica.simbolos.extend([])

        # No Terminales (incluímos epsilon porque en la tabla es un miembro de coordenada)
        epsilon = Simbolo(NoTerminal.epsilon, Simbolo.SimTipo.NO_TERMINAL)

        # Terminales
        peso = Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL)

        pass

    def load_prods(self):
        # TODO: Llenar la lista de producciones de G.
        # hint: 
        # self.gramatica.producciones.extend([])
        pass


    def load_table(self):
        # TODO: Llenar la tabla LL(1)
        # hint:
        # self.tabla[s] = {} 
        # self.tabla[s][numero] = Produccion(?, [?,?,...,?])
        pass

    def parse(self):
        self.load_syms()
        self.load_prods()
        self.load_table()
        # TODO: Implementar el algoritmo de An. Sintáctico LL(1)
        """
        Sea w una cadena de entrada (código fuente), STACK una pila, X un símbolo no terminal, Yi ∈ NUT y M una tabla de Análisis Sintáctico LL(1), 
        1. ip := w[0], x := top(STACK)
        2. Mientras x ≠ $ hacer:
            a. Si x == ip, entonces pop(STACK); ip++;
            b. si no, si x ∈ T: error( );
            c. si no, si M[x, ip] == ☐: error( );
            d. si no, si M[x, ip] == X ⟶ Y1Y2 ... Yk:
                i. imprimir X ⟶ Y1Y2 ... Yk ;
                ii. STACK.pop();
                iii. STACK.push(Yk,Yk-1, ..., Y2, Y1); 
                    Nota: Epsilon puede omitirse del push dado que no es un símbolo o manejarse de otra manera en las condiciones a.-d.
            e. x := top(STACK)
        """
        print("La cadena es aceptada?") # FIXME: Además de imprimir este mensaje, debemos devoler las derivaciones necesarias para construir la entrada.


    