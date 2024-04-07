def mostrar_asignaturas(asignaturas):
    """
    Función para mostrar la lista de asignaturas por pantalla.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.

    Returns:
    None
    """
    # Imprime un encabezado
    print("Lista de asignaturas:")
    
    # Itera sobre la lista de asignaturas
    for asignatura in asignaturas:
        # Imprime cada asignatura precedida por un guion
        print("- " + asignatura)


# Ejercicio 1
# Definición de una lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua","sociales "]
# Llama a la función mostrar_asignaturas con la lista de asignaturas como argumento
mostrar_asignaturas(asignaturas)
#define una función para imprimir una lista de asignaturas y luego la utiliza para imprimir la lista de asignaturas proporcionada en  ejercicio de uso al final.
