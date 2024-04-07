def ingresar_notas(asignaturas):
    """
    Función para solicitar al usuario ingresar las notas correspondientes a cada asignatura.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.

    Returns:
    - Una tupla que contiene una lista de asignaturas y una lista de notas ingresadas por el usuario.
    """
    notas = []
    for asignatura in asignaturas:
        nota = float(input(f"Ingrese la nota para {asignatura}: "))
        notas.append(nota)
    return asignaturas, notas


def obtener_asignaturas_repetir(asignaturas, notas):
    """
    Función para obtener las asignaturas que deben repetirse según las notas ingresadas.

    Args:
    - asignaturas: Una lista de cadenas que representan las asignaturas del curso.
    - notas: Una lista de notas ingresadas por el usuario, en el mismo orden que las asignaturas.

    Returns:
    - Una lista de asignaturas que el usuario debe repetir.
    """
    # Utilizando comprensión de listas para obtener las asignaturas que deben repetirse
    asignaturas_repetir = [asignatura for asignatura, nota in zip(asignaturas, notas) if nota < 5]
    return asignaturas_repetir


# Definir las asignaturas
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

# Solicitar al usuario ingresar las notas y obtener las asignaturas ingresadas
asignaturas_ingresadas, notas = ingresar_notas(asignaturas)

# Obtener las asignaturas que deben repetirse
asignaturas_repetir = obtener_asignaturas_repetir(asignaturas_ingresadas, notas)

# Mostrar las asignaturas que deben repetirse
if asignaturas_repetir:
    print("Debes repetir las siguientes asignaturas:", ", ".join(asignaturas_repetir))
else:
    print("¡Enhorabuena! No tienes que repetir ninguna asignatura.")
