def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para almacenar las palabras y su frecuencia
    frecuencia_palabras = {}

    for palabra in palabras:
        # Eliminar signos de puntuación y convertir a minúsculas
        palabra = palabra.strip('.,!?').lower()

        # Incrementar la frecuencia de la palabra en el diccionario
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

def palabra_mas_repetida(diccionario):
    # Encontrar la palabra más repetida y su frecuencia
    palabra_max = ""
    frecuencia_max = 0

    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia

    return (palabra_max, frecuencia_max)

# Ejemplo de uso
cadena = "Esta es una prueba. Esto es solo una prueba. Prueba esto y aquello."
diccionario = contar_palabras(cadena)
palabra_mas_rep = palabra_mas_repetida(diccionario)

print("Diccionario de frecuencias:")
print(diccionario)
print("Palabra más repetida y su frecuencia:")
print(palabra_mas_rep)
