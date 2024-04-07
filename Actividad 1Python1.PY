# Función para solicitar la edad del usuario
def solicitar_edad():
    while True:
        edad_input = input("Ingresa tu edad: ")  # Solicita al usuario que ingrese su edad
        try:
            edad = int(edad_input)  # Intenta convertir la entrada a un entero
            return edad  # Devuelve la edad si se pudo convertir con éxito
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")  # Muestra un mensaje de error si la entrada no es un entero válido

# Función para solicitar la cantidad de dinero en la billetera del usuario
def solicitar_dinero_en_billetera():
    while True:
        dinero_input = input("Ingresa la cantidad de dinero en tu billetera en dólares: ")  # Solicita al usuario que ingrese la cantidad de dinero en su billetera
        try:
            dinero = float(dinero_input)  # Intenta convertir la entrada a un número flotante
            return dinero  # Devuelve la cantidad de dinero si se pudo convertir con éxito
        except ValueError:
            print("Error: Por favor, ingresa una cantidad válida de dinero.")  # Muestra un mensaje de error si la entrada no es una cantidad de dinero válida

# Función para imprimir un mensaje personalizado según la edad del usuario
def imprimir_mensaje_segun_edad(edad):
    if edad < 18:
        return "menor de edad"  # Retorna un mensaje si el usuario es menor de 18 años
    elif 18 <= edad < 65:
        return "mayor de edad"  # Retorna un mensaje si el usuario tiene entre 18 y 64 años
    elif edad >= 65:
        return "de la tercera edad"  # Retorna un mensaje si el usuario tiene 65 años o más

# Función para solicitar al usuario si le gusta el clima caliente y asignar el valor a la variable correspondiente
def solicitar_preferencia_clima_caliente():
    while True:
        clima_caliente_input = input("¿Te gusta el clima caliente? (True/False): ")  # Solicita al usuario que ingrese si le gusta o no el clima caliente
        if clima_caliente_input.lower() == "true":
            return True  # Devuelve True si al usuario le gusta el clima caliente
        elif clima_caliente_input.lower() == "false":
            return False  # Devuelve False si al usuario no le gusta el clima caliente
        else:
            print("Error: Por favor, ingresa True o False.")  # Muestra un mensaje de error si la entrada no es "true" o "false"

# Solicitar la edad del usuario.
edad = solicitar_edad()  # Llama a la función solicitar_edad para obtener la edad del usuario

# Solicitar la cantidad de dinero en la billetera del usuario.
dinero_en_billetera = solicitar_dinero_en_billetera()  # Llama a la función solicitar_dinero_en_billetera para obtener la cantidad de dinero en la billetera del usuario

# Definir la variable que contiene el nombre de mi comida favorita
comida_favorita = "Sushi"  # Define una variable que contiene el nombre de la comida favorita
23
# Solicitar si le gusta o no el clima caliente
me_gusta_el_clima_caliente = solicitar_preferencia_clima_caliente()

# Imprimir mensaje personalizado según la edad ingresada
mensaje_edad = imprimir_mensaje_segun_edad(edad)

# Imprime si me gusta o no el clima caliente
print("¿Te gusta el clima caliente?", me_gusta_el_clima_caliente)  
# Imprimir todos los detalles
print("Eres una persona", mensaje_edad, "de", edad, "años, tu comida favorita es", comida_favorita, "y tienes", dinero_en_billetera, "dólares en tu billetera.")

