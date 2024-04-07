def pedir_numeros_ganadores():
    """
    Función para solicitar al usuario los números ganadores de la lotería.

    Returns:
    - Una lista de números ganadores ingresados por el usuario.
    """
    numeros_ganadores = input("Ingrese los números ganadores de la lotería separados por espacios: ").split()
    return numeros_ganadores


# Ejercicio 4
# Llamada a la función para pedir al usuario los números ganadores
numeros_ganadores = pedir_numeros_ganadores()

# Imprimir los números ganadores ingresados por el usuario
print("Los números ganadores de la lotería son:", numeros_ganadores)

#Define una función pedir_numeros_ganadores() que solicita al usuario ingresar los números ganadores de la lotería, separados por espacios. Luego, el programa llama a esta función y muestra los números ganadores ingresados por el usuario.

#Es importante notar que split() se utiliza para dividir la entrada del usuario en una lista de números, separados por espacios.
