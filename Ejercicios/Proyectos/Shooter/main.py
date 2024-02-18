import random

# Definir la cantidad inicial de munición y la puntuación del jugador
munición = 6  # Se reduce la munición a 6 balas
puntuación = 0

# Función para simular el disparo del jugador
def disparar():
    global munición, puntuación
    if munición > 0:
        # Simular si el disparo alcanza un objetivo (50% de probabilidad de éxito)
        if random.random() < 0.5:
            print("¡Has acertado al objetivo!")
            puntuación += 10
        else:
            print("Has fallado el objetivo.")
        munición -= 1
    else:
        print("¡Te has quedado sin munición! Recarga tu arma.")

# Función para recargar el arma
def recargar():
    global munición
    # Recargar el arma con 6 balas
    munición = min(munición + 6, 6)  # Se recargan 6 balas
    print("Has recargado tu arma con 6 balas. Munición restante:", munición)

# Función para generar objetivos aleatorios
def generar_objetivos(n):
    objetivos = ["enemigo", "objetivo neutral", "amigo"]
    return random.choices(objetivos, k=n)

# Juego principal
print("¡Bienvenido al simulador de disparos en un juego shooter!")

while True:
    print("\nOpciones:")
    print("1. Disparar")
    print("2. Recargar")
    print("3. Salir")

    opción = input("Elige una opción: ")

    if opción == "1":
        disparar()
    elif opción == "2":
        recargar()
    elif opción == "3":
        print("¡Gracias por jugar!")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

# Mostrar la puntuación al final del juego
print("Tu puntuación final es:", puntuación)
