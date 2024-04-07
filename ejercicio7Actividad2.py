def eliminar_multiplos_de_tres(abecedario):
    """
    Función para eliminar las letras del abecedario que ocupan posiciones múltiplos de 3.

    Args:
    - abecedario: Una lista de letras del abecedario.

    Returns:
    - Una lista con las letras del abecedario filtradas.
    """
    abecedario_filtrado = [letra for indice, letra in enumerate(abecedario, start=1) if indice % 3 != 0]
    return abecedario_filtrado


# Crear el abecedario
abecedario = [chr(i) for i in range(97, 123)]

# Eliminar las letras que ocupan posiciones múltiplos de 3
abecedario_filtrado = eliminar_multiplos_de_tres(abecedario)

# Mostrar por pantalla la lista resultante
print(abecedario_filtrado)

#Este programa almacena el abecedario en una lista, 
#luego utiliza una función llamada eliminar_multiplos_de_tres 
#para eliminar las letras que ocupan posiciones múltiplos de 3. Finalmente,
#muestra por pantalla la lista resultante.





