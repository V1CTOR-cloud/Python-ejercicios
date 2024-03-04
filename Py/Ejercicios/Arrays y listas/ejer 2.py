import random

def generar_plataformas(num_plataformas, altura_maxima, ancho_nivel):
    try:
        # Control datos
        if not isinstance(num_plataformas, int) or not isinstance(altura_maxima, int) or not isinstance(ancho_nivel, int):
            raise TypeError("Los parámetros deben ser enteros.")
        if num_plataformas <= 0 or altura_maxima <= 0 or ancho_nivel <= 0:
            raise ValueError("Los parámetros deben ser mayores que cero.")

        # Asignacion plataformas
        plataformas = []
        for _ in range(num_plataformas):
            posicion = random.randint(0, ancho_nivel)
            altura = random.randint(0, altura_maxima)
            plataformas.append((posicion, altura))
        
        return plataformas
    
    except TypeError as te:
        print(f"Error: {te}")
        return []
    except ValueError as ve:
        print(f"Error: {ve}")
        return []

# Solicitar los parámetros al usuario
try:
    num_plataformas = int(input("Ingrese el número de plataformas a generar: "))
    altura_maxima = int(input("Ingrese la altura máxima de las plataformas: "))
    ancho_nivel = int(input("Ingrese el ancho total del nivel del juego: "))

    plataformas = generar_plataformas(num_plataformas, altura_maxima, ancho_nivel)
    print("Plataformas generadas:")
    for plataforma in plataformas:
        print(f"Posición: {plataforma[0]}, Altura: {plataforma[1]}")
                        
        
        

except ValueError:
    print("Error: Por favor, ingrese valores enteros válidos para los parámetros.")