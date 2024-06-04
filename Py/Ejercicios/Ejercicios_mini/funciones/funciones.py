def filtrar_palabras(lista_palabras, longitud_minima):
    palabras_filtradas = []
    for palabra in lista_palabras:
        if len(palabra) >= longitud_minima:
            palabras_filtradas.append(palabra)
    return palabras_filtradas

palabras = ["hola", "bienvenido", "a", "este", "ejercicio", "ejem"]
longitud_minima = 5

palabras_filtradas = filtrar_palabras(palabras, longitud_minima)
print("Palabras filtradas:", palabras_filtradas)
