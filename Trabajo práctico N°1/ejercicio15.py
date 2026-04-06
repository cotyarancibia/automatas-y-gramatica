"""
Escribir una expresión regular que valide una dirección de mail 
según estas reglas:
• Nombre de usuario: letras mayúsculas, minúsculas, números y 
solo los caracteres especiales guion medio ( - ) y guion bajo ( _ ).
• Debe haber exactamente un símbolo @ separando usuario y dominio.
• Dominio: solo letras mayúsculas, minúsculas y números 
(sin caracteres especiales).
• Extensión: entre 2 y 4 letras (ej: .com, .org, .edu, .info)
"""

import re

mail = input("Ingrese una dirección de mail: ") 

patron= r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'

if re.match(patron, mail):
    print("La dirección de mail es válida.")
else:
    print("La dirección de mail no es válida.")
