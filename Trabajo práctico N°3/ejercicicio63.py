# Parser descendente recursivo simple
# La idea es recorrer la gramática usando funciones
# y avanzar en la lista de tokens con un índice

def parsear(tokens):
    i = 0  # posición actual en la lista

    def error(msg):
        raise Exception(f"Error en posición {i}: {msg}")

    # E → T E'
    def E():
        print("Aplicando E → T E'")
        T()
        Ep()

    # E' → + T E' | ε
    def Ep():
        nonlocal i
        if i < len(tokens) and tokens[i] == '+':
            print("Aplicando E' → + T E'")
            i += 1  # consumo el +
            T()
            Ep()
        else:
            print("Aplicando E' → ε")

    # T → F T'
    def T():
        print("Aplicando T → F T'")
        F()
        Tp()

    # T' → * F T' | ε
    def Tp():
        nonlocal i
        if i < len(tokens) and tokens[i] == '*':
            print("Aplicando T' → * F T'")
            i += 1  # consumo el *
            F()
            Tp()
        else:
            print("Aplicando T' → ε")

    # F → num | (E)
    def F():
        nonlocal i
        if i < len(tokens) and tokens[i] == 'num':
            print("Aplicando F → num")
            i += 1  # consumo num
        elif i < len(tokens) and tokens[i] == '(':
            print("Aplicando F → (E)")
            i += 1  # consumo (
            E()
            if i < len(tokens) and tokens[i] == ')':
                i += 1  # consumo )
            else:
                error("faltaba ')'")
        else:
            error("se esperaba num o (")

    # empieza el parsing desde E
    E()

    # si consumí todos los tokens → OK
    if i == len(tokens):
        print("Resultado: ACEPTADO ✔")
    else:
        error("sobran tokens")