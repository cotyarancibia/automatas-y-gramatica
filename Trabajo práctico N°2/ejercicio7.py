"""AFD para la expresión (a|b)*abb
Estados: A, B, C, D, E
Estado inicial: A
Estado de aceptación: E"""

def afd(cadena):
    estado = 'A'  #estado inicial

    for simbolo in cadena:
        if estado == 'A':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo == 'b':
                estado = 'C'
            else:
                return False

        elif estado == 'B':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo == 'b':
                estado = 'D'
            else:
                return False

        elif estado == 'C':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo == 'b':
                estado = 'C'
            else:
                return False

        elif estado == 'D':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo == 'b':
                estado = 'E'
            else:
                return False

        elif estado == 'E':
            if simbolo == 'a':
                estado = 'B'
            elif simbolo == 'b':
                estado = 'C'
            else:
                return False

    # Acepta solo si termina en E
    return estado == 'E'


# Pruebas 
cadenas = ["abb", "aabb", "babb", "ab", "abba", "bbabb"]

for c in cadenas:
    if afd(c):
        print(f"{c} -> ACEPTADA")
    else:
        print(f"{c} -> RECHAZADA")