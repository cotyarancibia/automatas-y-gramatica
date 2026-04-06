"""
EJERCICIO N° 10 Limpieza de datos	
Imaginen que el sistema de alumnos recibió inscripciones 
a las mesas de exámenes, pero los nombres ingresados tienen 
un formato caótico. Algunos están en mayúsculas, 
otros en minúsculas y muchos contienen espacios extra innecesarios 
al principio o al final de la cadena. 
Escriban una función que reciba uno de estos strings desordenados 
y lo devuelva en formato "Título" (solo la primera letra en 
mayúscula), eliminando cualquier espacio sobrante en los extremos.
Exploren los métodos nativos que los objetos string de Python 
ya nos ofrecen para limpiar y transformar texto sin usar librerías
externas.
Input de ejemplo:
"JUAN pablo DOMINGUEZ"

Output esperado:
"Juan Pablo Dominguez"
"""

nombre= input("Ingrese el nombre del alumno: ")

def ordenar_nombre(nombre):
    nombre_limpio= nombre.strip()
    nombre_ordenado= nombre_limpio.title()
    return nombre_ordenado

print(ordenar_nombre(nombre))   