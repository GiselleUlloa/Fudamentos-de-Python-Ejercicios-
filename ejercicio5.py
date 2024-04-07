def pedir_numeros_ganadores():
    """
    Función para solicitar al usuario los números ganadores de la lotería primitiva.

    Returns:
    - Una lista de números ganadores ingresados por el usuario.
    """
    numeros_ganadores = input("Ingrese los números ganadores de la lotería primitiva separados por espacios: ").split()
    return numeros_ganadores


def ordenar_numeros_ganadores(numeros_ganadores):
    """
    Función para ordenar los números ganadores de la lotería primitiva.

    Args:
    - numeros_ganadores: Una lista de números enteros que representan los números ganadores.

    Returns:
    - Una lista de números ganadores ordenados de menor a mayor.
    """
    numeros_ganadores = [int(numero) for numero in numeros_ganadores]
    numeros_ganadores.sort()
    return numeros_ganadores


# Solicitar al usuario los números ganadores
numeros_ganadores = pedir_numeros_ganadores()

# Ordenar los números ganadores
numeros_ganadores_ordenados = ordenar_numeros_ganadores(numeros_ganadores)

# Mostrar los números ganadores ordenados de menor a mayor en pantalla como una lista
print("Números ganadores ordenados de menor a mayor:")
print("[{}]".format(", ".join(map(str, numeros_ganadores_ordenados))))
