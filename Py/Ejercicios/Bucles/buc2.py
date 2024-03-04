import random

# Solicitar al usuario que ingrese los nombres de los jugadores
print("Introduce los nombres de los jugadores:")
jugadores = [input("Jugador {}: ".format(i+1)) for i in range(10)]

# Elegir un impostor aleatorio de la lista de jugadores
impostor = random.choice(jugadores)

print("\n¡Bienvenido al juego Encuentra al Impostor!")
print("Debes adivinar quién es el impostor entre los jugadores.")
print("Tienes 3 intentos para adivinar correctamente.")

intentos = 0

# Bucle while para continuar el juego hasta que el jugador agote los intentos o adivine al impostor
while intentos < 3:
    # Mostrar los nombres de los jugadores para que el jugador haga su elección
    print("\nElige un jugador:")
    for index, jugador in enumerate(jugadores, start=1):
        print(f"{index}. {jugador}")


    opcion = int(input("Introduce el número del jugador que crees que es el impostor: "))
 
    # Verificar si la opción seleccionada es el impostor
    if opcion < 1 or opcion > len(jugadores):
        print("Opción inválida. Inténtalo de nuevo.")
        continue

    jugador_elegido = jugadores[opcion - 1]

    if jugador_elegido == impostor:
        print("¡Felicidades! ¡Has encontrado al impostor! El impostor era:", impostor)
        break
    else:
        print("Ese jugador no es el impostor. Inténtalo de nuevo.")
        intentos += 1


# Si el jugador agotó los intentos sin adivinar al impostor, mostrar al impostor
if intentos == 3:
    print("\n¡Lo siento! Has agotado tus intentos. El impostor era:", impostor)