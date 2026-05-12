from collections import deque
class GramaticaGLC:
    def __init__(self, terminales, no_terminales, simbolo_inicial, producciones):
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.simbolo_inicial = simbolo_inicial
        self.producciones = producciones

    def derivar_izquierda(self, cadena):
        print("Derivación por izquierda:\n")
        actual = self.simbolo_inicial
        paso = 1
        print(f"Paso {paso}: {actual}")
        while actual != cadena:
            indice = actual.find('S')
            if indice == -1:
                print("No se pudo derivar la cadena.")
                return
            cantidad_a = actual.count('a')
            objetivo_a = cadena.count('a')

            # Mientras falten 'a'
            if cantidad_a < objetivo_a - 1:
                nueva = (
                        actual[:indice]
                        + 'aSb'
                        + actual[indice + 1:]
                )
            else:
                nueva = (
                        actual[:indice]
                        + 'ab'
                        + actual[indice + 1:]
                )
            actual = nueva
            paso += 1
            print(f"Paso {paso}: {actual}")

    def derivar_derecha(self, cadena):
        print("Derivación por derecha:\n")
        actual = self.simbolo_inicial
        paso = 1
        print(f"Paso {paso}: {actual}")
        while actual != cadena:
            indice = actual.rfind('S')
            if indice == -1:
                print("No se pudo derivar la cadena.")
                return
            cantidad_a = actual.count('a')
            objetivo_a = cadena.count('a')
            if cantidad_a < objetivo_a - 1:
                nueva = (
                        actual[:indice]
                        + 'aSb'
                        + actual[indice + 1:]
                )
            else:
                nueva = (
                        actual[:indice]
                        + 'ab'
                        + actual[indice + 1:]
                )
            actual = nueva
            paso += 1
            print(f"Paso {paso}: {actual}")
    def pertenece(self, cadena):
        cola = deque()
        cola.append(self.simbolo_inicial)
        visitados = set()
        while cola:
            actual = cola.popleft()
            if actual == cadena:
                return True
            if actual in visitados:
                continue
            visitados.add(actual)
            if len(actual) > len(cadena) + 2:
                continue
            for i, caracter in enumerate(actual):
                if caracter in self.no_terminales:
                    for produccion in self.producciones[caracter]:
                        nueva = (
                                actual[:i]
                                + produccion
                                + actual[i + 1:]
                        )

                        cola.append(nueva)

        return False
g = GramaticaGLC(
    terminales={'a', 'b'},
    no_terminales={'S'},
    simbolo_inicial='S',
    producciones={
        'S': ['aSb', 'ab']
    }
)
g.derivar_izquierda('aaabbb')
print()
g.derivar_derecha('aaabbb')
print()
print(g.pertenece('aaabbb'))   # True
print(g.pertenece('aabb'))     # True
print(g.pertenece('aabbb'))    # False