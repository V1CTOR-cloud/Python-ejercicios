import random

def generar_posiciones_gemas(num_gemas, ancho_nivel):
    try:
        # Validar los parámetros
        # controlamos que son números, si no levantamos una excepeción
        if not isinstance(num_gemas, int) or not isinstance(ancho_nivel, int):
            raise TypeError("Los parámetros deben ser enteros.")
        if num_gemas <= 0 or ancho_nivel <= 0:
            raise ValueError("Los parámetros deben ser mayores que cero.")

        # Generar las posiciones de las gemas
        # NO hacemos uso de la posicion (i)
        posiciones_gemas = []
        for _ in range(num_gemas):
            posicion = random.randint(0, ancho_nivel)
            posiciones_gemas.append(posicion)
        
        return posiciones_gemas
    
    
    
    except TypeError as te:
        print(f"Error: {te}")
        return [] # Lo mismo que pass
    except ValueError as ve:
        print(f"Error: {ve}")
        return [] # Lo mismo que pass

# Solicitar los parámetros al usuario
try:
    num_gemas = int(input("Ingrese el número de gemas a generar: "))
    ancho_nivel = int(input("Ingrese el ancho total del nivel del juego: "))

    posiciones_gemas = generar_posiciones_gemas(num_gemas, ancho_nivel)
    if posiciones_gemas:
        print("Posiciones de las gemas generadas:")
        print(posiciones_gemas)
    else:
        print("No se han generado gemas.")

except ValueError:
    print("Error: Por favor, ingrese valores enteros válidos para los parámetros.")
