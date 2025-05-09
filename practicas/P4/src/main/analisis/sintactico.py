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
        """
        Carga los símbolos de la gramática en la lista de símbolos.
        :return: None
        """
        # TODO: Llenar la lista de símbolos de G.
        # hint: self.gramatica.simbolos.extend([])

        # No Terminales (incluímos epsilon porque en la tabla es un miembro de coordenada)
        # epsilon = Simbolo(NoTerminal.EPSILON, Simbolo.SimTipo.NO_TERMINAL)

        # Solucion no optima, pero funcional

        # No Terminales
        #self.gramatica.simbolos.extend([
        #    Simbolo(NoTerminal.S, Simbolo.SimTipo.NO_TERMINAL),
        #    Simbolo(NoTerminal.SPRIM, Simbolo.SimTipo.NO_TERMINAL),
        #    Simbolo(NoTerminal.EPSILON, Simbolo.SimTipo.NO_TERMINAL),
        #])

        # Terminales
        #self.gramatica.simbolos.extend([
        #    Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL),
        #    Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL),
        #    Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL),
        #])

        # Solucion optima usando un diccionario
        # No Terminales
        self.gramatica.add_sim(Simbolo(NoTerminal.S, Simbolo.SimTipo.NO_TERMINAL))
        self.gramatica.add_sim(Simbolo(NoTerminal.SPRIM, Simbolo.SimTipo.NO_TERMINAL))
        self.gramatica.add_sim(Simbolo(NoTerminal.EPSILON, Simbolo.SimTipo.NO_TERMINAL))

        # Terminales
        self.gramatica.add_sim(Simbolo(ClaseLexica.NUMERO, Simbolo.SimTipo.TERMINAL))
        self.gramatica.add_sim(Simbolo(ClaseLexica.PLUS, Simbolo.SimTipo.TERMINAL))
        self.gramatica.add_sim(Simbolo(ClaseLexica.EOF, Simbolo.SimTipo.TERMINAL))

    def load_prods(self):
        """
        Carga las producciones de la gramática en la lista de producciones.
        :return: None
        """

        # TODO: Llenar la lista de producciones de G.
        # hint: 
        # self.gramatica.producciones.extend([])
        get = self.gramatica.get_sim

        self.gramatica.producciones.extend([
        Produccion(get(NoTerminal.S), [get(ClaseLexica.NUMERO), get(NoTerminal.SPRIM)]),
        Produccion(get(NoTerminal.SPRIM), [get(ClaseLexica.PLUS), get(ClaseLexica.NUMERO),
                                            get(NoTerminal.SPRIM)]),
        Produccion(get(NoTerminal.SPRIM), [get(NoTerminal.EPSILON)])
        ])


    def load_table(self):
        """
        Carga la tabla LL(1) de la gramática.
        :return: None
        """

        # TODO: Llenar la tabla LL(1)
        # hint:
        # self.tabla[s] = {} 
        # self.tabla[s][numero] = Produccion(?, [?,?,...,?])
        get = self.gramatica.get_sim
        

        # Inicializamos la tabla
        self.tabla = {}

        # Símbolos
        S      = get(NoTerminal.S)
        SPRIM  = get(NoTerminal.SPRIM)
        EPS    = get(NoTerminal.EPSILON)

        NUM    = get(ClaseLexica.NUMERO)
        PLUS   = get(ClaseLexica.PLUS)
        EOF    = get(ClaseLexica.EOF)

        # Producciones
        prod_S      = self.gramatica.producciones[0]  # S → NUMERO SPRIM
        prod_SPRIM1 = self.gramatica.producciones[1]  # SPRIM → PLUS NUMERO SPRIM
        prod_SPRIM2 = self.gramatica.producciones[2]  # SPRIM → ε

        # Fila S
        self.tabla[S] = {
            NUM: prod_S
        }

        # Fila SPRIM
        self.tabla[SPRIM] = {
            PLUS: prod_SPRIM1,
            EOF: prod_SPRIM2
        }

    def parse(self):
        """
        Función principal del analizador sintáctico.
        :return: None
        """
        

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

        self.an_lexico.lexer.input(self.an_lexico.lexer.lexdata)  # reiniciar entrada

        # Inicializamos
        stack = []
        get = self.gramatica.get_sim

        # Símbolos iniciales
        S = get(NoTerminal.S)
        EOF = get(ClaseLexica.EOF)

        stack.append(EOF)  # Símbolo $
        stack.append(S)

        tok = self.an_lexico.lexer.token()
        if not tok:
            self.error("Entrada vacía")
            return

        a = ClaseLexica[tok.type]  # primer token

        while len(stack) > 0:
            X = stack[-1]  # tope de la pila

            if X.tipo == X.SimTipo.TERMINAL:
                if X.sim == a:
                    stack.pop()
                    tok = self.an_lexico.lexer.token()
                    if tok:
                        a = ClaseLexica[tok.type]
                    else:
                        a = ClaseLexica.EOF
                else:
                    self.error(f"Se esperaba {X.sim.name}, pero se encontró {a.name}")
            elif X.tipo == X.SimTipo.NO_TERMINAL:
                fila = self.tabla.get(X)
                if not fila:
                    self.error(f"No hay fila para {X.sim.name}")
                produccion = fila.get(get(a))
                if not produccion:
                    self.error(f"No hay producción para [{X.sim.name}, {a.name}]")

                # Imprimir producción aplicada
                cabeza = produccion.cabeza.sim.name

                cuerpo = [s.sim.name for s in produccion.cuerpo]
                print(f"{cabeza} → {' '.join(cuerpo) if cuerpo else 'ε'}")

                stack.pop()
                # Push en orden inverso
                for simbolo in reversed(produccion.cuerpo):
                    if simbolo.sim != NoTerminal.EPSILON:
                        stack.append(simbolo)
            else:
                self.error("Símbolo desconocido en la pila")

        if a == ClaseLexica.EOF:
            print("Cadena aceptada")
        else:
            self.error("Quedaron símbolos sin analizar")
            print("Cadena rechazada")



    