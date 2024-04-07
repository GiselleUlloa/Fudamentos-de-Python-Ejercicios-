def contar_vocales(palabra):
    """
    Función para contar el número de veces que aparece cada vocal en una palabra.

    Args:
    - palabra: Una cadena que representa la palabra de la cual se contarán las vocales.

    Returns:
    - Un diccionario donde las claves son las vocales ('a', 'e', 'i', 'o', 'u') y los valores son los conteos de cada vocal.
    """
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para asegurar la comparación
    vocales = ['a', 'e', 'i', 'o', 'u']  # Lista de vocales
    # Crear un diccionario con comprensión de diccionarios donde las claves son las vocales y los valores son los conteos
    conteo_vocales = {vocal: palabra.count(vocal) for vocal in vocales}
    return conteo_vocales


# Ejercicio 9
palabra = input("Ingrese una palabra: ")  # Solicitar al usuario ingresar una palabra
conteo_vocales = contar_vocales(palabra)  # Contar las vocales en la palabra
print(conteo_vocales)  # Imprimir el conteo de las vocales
