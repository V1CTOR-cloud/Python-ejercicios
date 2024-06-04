import time

def detonar_bomba():
    print("¡BUM!")

def temporizador(callback, tiempo):
    while tiempo > 0:
        print(tiempo)
        time.sleep(1)  # Espera 1 segundo
        tiempo -= 1
    callback()

print("La bomba ha sido activada. ¡Corre!")
temporizador(detonar_bomba, 5)