
class Gramatica:
    def __init__ (self,terminales, no_terminales, simbolo_inicial,producciones):
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.simbolo_inicial = simbolo_inicial
        self.producciones = producciones

    # Tipo 3
    def es_regular(self):
        for izq in self.producciones:
            if izq not in self.no_terminales:
                return False
            
            reglas = self.producciones[izq]
            
            for regla in reglas:
                if regla == 'ε':
                    continue

                longitud = len(regla)

                if longitud == 1:
                    simbolo = regla[0]

                    if simbolo in self.terminales:
                        continue
                    else:
                        return False
            
                elif longitud == 2:
                    primer = regla[0]
                    segundo = regla[1]

                    if primer in self.terminales and segundo in self.no_terminales:
                        continue
                    else:
                        return False
                else:
                    return False
            
        return True
            
    # Tipo 2
    def es_glc(self):
        for izq in self.producciones:
            if izq not in self.no_terminales:
                return False
        return True
    
        
    def clasificar(self):
        if self.es_regular():
            return "Tipo 3: Regular"
        elif self.es_glc():
            return "Tipo 2: Libre de Contexto"
        else:
            return "Tipo 0 o 1"
        
    def __str__(self):
        lineas = []
        for izq in self.producciones:
            reglas = self.producciones[izq]

            derecha = " | ".join(reglas)

            linea = izq + " -> " + derecha
            lineas.append(linea)

        resultado = "\n".join(lineas)
        return resultado
        
def cargar_desde_texto(texto):
    producciones = {}
    terminales = set()
    no_terminales = set()

    lineas = texto.strip().split("\n")

    for linea in lineas:
        linea = linea.strip()
        if not linea:
            continue

        izq, derecha = linea.split(" -> ")
        izq = izq.strip()
        derecha = derecha.strip()

        no_terminales.add(izq)
        reglas = derecha.split(" | ")

        reglas_limpias = []

        for regla in reglas:
            regla = regla.strip()
            reglas_limpias.append(regla)

            for simbolo in regla:
                if simbolo.islower():
                    terminales.add(simbolo)

        producciones[izq] = reglas_limpias

    simbolo_inicial = lineas[0].split("->")[0].strip()
    return Gramatica(terminales, no_terminales, simbolo_inicial, producciones)

#Ejemplo de validación de cadenas (solo para un caso específico)
def validar_cadenas(g, cadena):
    cant_a = 0
    cant_b = 0

    for c in cadena:
        if c == "a":
            cant_a += 1
        elif c == "b":
            cant_b += 1
        else:
            return False
        
    return cant_a == cant_b and cadena == "a" * cant_a +"b" * cant_b

g = Gramatica(
    terminales={'a', 'b'},
    no_terminales={'S'},
    simbolo_inicial='S',
    producciones={'S': ['aSb', 'ε']}
)

print(g.clasificar())   #Tipo
print(g.es_regular())   #True/False
print(g.es_glc())       #True/False
print(g)                # Producciones


texto = '''
S -> aSb | ε
'''
g = cargar_desde_texto(texto)

print(g.clasificar())
print(g.es_regular())
print(g.es_glc())
print(g)


print("Validación de cadenas(a^n b^n): ")
print(validar_cadenas(g, "aabb"))   
print(validar_cadenas(g, "aaabbb")) 
print(validar_cadenas(g, "aab"))    
print(validar_cadenas(g, "abab"))
