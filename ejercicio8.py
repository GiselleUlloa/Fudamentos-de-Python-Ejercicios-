def es_palindromo(palabra):
    """
    Función para verificar si una palabra es un palíndromo.

    Args:
    - palabra: Una cadena que representa la palabra a verificar.

    Returns:
    - True si la palabra es un palíndromo, False en caso contrario.
    """
    return palabra == palabra[::-1]


# Ejercicio 8
palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")

#La función es_palindromo toma una cadena como entrada y devuelve 
#True si la palabra es un palíndromo, es decir, si se lee igual de 
#izquierda a derecha que de derecha a izquierda. Devuelve False
#en caso contrario. El programa principal solicita al usuario 
#ingresar una palabra, luego utiliza la función es_palindromo para determinar si es 
#un palíndromo y muestra un mensaje apropiado en consecuencia.