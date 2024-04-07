def estudiar_asignaturas(asignaturas):
    """
    Función para mostrar un mensaje indicando que se estudian las asignaturas.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.

    Returns:
    None
    """
    # Imprime un mensaje indicando que se estudian las asignaturas
    print("Asignaturas que estudio:")
    
    # Itera sobre la lista de asignaturas
    for asignatura in asignaturas:
        # Imprime cada asignatura precedida por "Yo estudio"
        print("- Yo estudio", asignatura)


# Ejercicio 2
# Lista de asignaturas a estudiar
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# Llama a la función estudiar_asignaturas con la lista de asignaturas como argumento
estudiar_asignaturas(asignaturas)
