def obtener_extremos(lista_numeros):
    """
    Función para obtener el valor mínimo y máximo de una lista de números.

    Args:
    - lista_numeros: Una lista de números.

    Returns:
    - El valor mínimo y máximo de la lista, en forma de tupla (min, max).
    """
    return min(lista_numeros), max(lista_numeros)


# Ejercicio 10
precios = [50, 75, 46, 22, 80, 65, 8]
minimo, maximo = obtener_extremos(precios)
print("El precio más bajo es:", minimo)
print("El precio más alto es:", maximo)
