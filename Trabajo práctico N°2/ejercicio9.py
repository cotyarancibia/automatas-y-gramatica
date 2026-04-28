"""Programa que valida comentarios de tipo /* ... */ usando un AFD.
El autómata trabaja sobre el alfabeto { '/', '*', 'a', 'b' } y no usa expresiones regulares."""

ALFABETO_COMENTARIO = {'/', '*', 'a', 'b'}

Q0_INICIO = 0
Q1_DESPUES_SLASH = 1
Q2_DENTRO_COMENTARIO = 2
Q3_PUEDE_CERRAR = 3
Q4_CERRADO = 4


def es_comentario_valido(cadena: str) -> bool:
    """Verifica si la cadena es un comentario válido del tipo /* ... */."""
    if not cadena:
        return False

    estado = Q0_INICIO

    for simbolo in cadena:
        if simbolo not in ALFABETO_COMENTARIO:
            return False

        if estado == Q0_INICIO:
            # q0: debemos recibir el primer '/'
            if simbolo == '/':
                estado = Q1_DESPUES_SLASH
            else:
                return False

        elif estado == Q1_DESPUES_SLASH:
            # q1: después de '/', debemos recibir '*' para iniciar el comentario
            if simbolo == '*':
                estado = Q2_DENTRO_COMENTARIO
            else:
                return False

        elif estado == Q2_DENTRO_COMENTARIO:
            # q2: dentro del comentario, aceptamos a, b, /, o '*' que puede ser el inicio del cierre
            if simbolo == '*':
                estado = Q3_PUEDE_CERRAR
            elif simbolo in {'a', 'b', '/'}:
                estado = Q2_DENTRO_COMENTARIO
            else:
                return False

        elif estado == Q3_PUEDE_CERRAR:
            # q3: ya vimos '*', puede ser el cierre si viene '/'
            if simbolo == '/':
                estado = Q4_CERRADO
            elif simbolo == '*':
                estado = Q3_PUEDE_CERRAR
            elif simbolo in {'a', 'b', '/'}:
                estado = Q2_DENTRO_COMENTARIO
            else:
                return False

        elif estado == Q4_CERRADO:
            # q4: comentario cerrado, no debe haber símbolos adicionales
            return False

    return estado == Q4_CERRADO


def probar() -> None:
    """Ejecuta casos de prueba representativos para el AFD."""
    pruebas = [
        # casos válidos
        '/**/',
        '/*ab*/',
        '/*a*b/a*/',
        '/*aaab*/',
        '/*////*/',

        # casos inválidos
        '',
        '/',
        '/*',
        '/**',
        '*/',
        '/*a*/x',
        '/* */',
        '/*ab',
        '/*abc*/',
        '/*a?*/',
        '/*ab*/*',
    ]

    for prueba in pruebas:
        resultado = es_comentario_valido(prueba)
        print(f"{prueba!r} → {resultado}")


if __name__ == '__main__':
    probar()