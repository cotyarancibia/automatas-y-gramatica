def simular_afd(cadena):
    estado = "A"

    finales = {"A", "B", "C"}

    transiciones = {
        "A": {"a": "B", "b": "C"},
        "B": {"a": "B", "b": "C"},
        "C": {"a": "B", "b": "C"}
    }

    for simbolo in cadena:
        if simbolo not in {"a", "b"}:
            return False
        estado = transiciones[estado][simbolo]

    return estado in finales


print(simular_afd(""))      # True
print(simular_afd("a"))     # True
print(simular_afd("b"))     # True
print(simular_afd("ab"))    # True
print(simular_afd("ba"))    # True
print(simular_afd("abba"))  # True
print(simular_afd("abc"))   # False