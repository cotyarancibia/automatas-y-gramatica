"""Dada la expresión regular: (a | b)*(a | b | ε)
"""
ALFABETO = {'a', 'b'}

def afn(cadena):
    return all(simbolo in ALFABETO for simbolo in cadena)


#Pruebas
cadenas = ["", "a", "b", "abba", "bbbaa", "ababab"]

for c in cadenas:
    if afn(c):
        print(f"'{c}' -> ACEPTADA")
    else:
        print(f"'{c}' -> RECHAZADA")