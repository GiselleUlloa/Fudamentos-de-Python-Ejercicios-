#se definen dos funciones:
#ingresar_notas: Esta función solicita al usuario ingresar las notas para cada asignatura en la lista de asignaturas proporcionada. Luego, devuelve una lista de notas en el mismo orden que las asignaturas.
#mostrar_notas: Esta función toma la lista de asignaturas y la lista de notas ingresadas por el usuario, y muestra las notas correspondientes a cada asignatura.

def ingresar_notas(asignaturas):
    """
    Función para solicitar al usuario las notas de cada asignatura.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.

    Returns:
    - Una lista de notas ingresadas por el usuario, en el mismo orden que las asignaturas.
    """
    notas = []
    for asignatura in asignaturas:
        nota = float(input("Ingrese la nota de {}: ".format(asignatura)))
        notas.append(nota)
    return notas


def mostrar_notas(asignaturas, notas):
    """
    Función para mostrar las notas ingresadas por el usuario.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.
    - notas: Una lista de notas ingresadas por el usuario, en el mismo orden que las asignaturas.

    Returns:
    None
    """
    print("Notas ingresadas:")
    for i in range(len(asignaturas)):
        print("- En {} has sacado {}".format(asignaturas[i], notas[i]))


# Ejercicio 3
# Lista de asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
# Solicitar al usuario ingresar las notas
notas = ingresar_notas(asignaturas)
# Mostrar las notas ingresadas por el usuario
mostrar_notas(asignaturas, notas)

 #que consiste en solicitar al usuario que ingrese las notas para las asignaturas especificadas y luego mostrar esas notas junto con las asignaturas correspondientes.
