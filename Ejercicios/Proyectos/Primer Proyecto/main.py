vida = 100
dañoBase = 25

print("Vas a equipar a tu personaje, primero elige tu armadura")
print("Las opciones son: 1. Armadura diamante 2. Armadura hierro 3. Armadura cuero")

while True:
    ARMADURA = int(input('Pon el número de la opción que quieras: '))
    if 1 <= ARMADURA <= 3:
        break
    else:
        print('Opción no válida, escoja una de las opciones')

if ARMADURA == 1:
    vida += 100  # Aumento de vida corregido para armadura de diamante
elif ARMADURA == 2:
    vida += 75  # Aumento de vida corregido para armadura de hierro
else:
    vida += 50  # Aumento de vida corregido para armadura de cuero

print('Ahora debes elegir tu arma; las opciones son: 1. Espada diamante 2. Espada hierro 3. Espada madera')

while True:
    ARMA = int(input('Pon el número de la opción que quieras: '))
    if 1 <= ARMA <= 3:
        break
    else:
        print('Opción no válida, escoja una de las opciones')

if ARMA == 1:
    dañoBase += 25  # Aumento de daño corregido para espada de diamante
elif ARMA == 2:
    dañoBase += 10  # Aumento de daño corregido para espada de hierro
else:
    dañoBase += 5  # Aumento de daño corregido para espada de madera

print('Por último elija la poción que desea tener entre las siguientes: 1. Poción legendaria 2. Poción mítica 3. Poción simple')

while True:
    POCION = int(input('Pon el número de la opción que quieras: '))
    if 1 <= POCION <= 3:
        break
    else:
        print('Opción no válida, escoja una de las opciones')

if POCION == 1:
    vida += 100  # Aumento de vida corregido para poción legendaria
elif POCION == 2:
    vida += 50  # Aumento de vida corregido para poción mítica
else:
    vida += 25  # Aumento de vida corregido para poción simple

print('Tu vida actual es:', vida)
print('Tu daño actual es', dañoBase)

nEnemigos = int(input('Contra cuántos enemigos te quieres enfrentar? '))
ELIGERO = EMEDIO = EPESADO = 0

for i in range(nEnemigos):
    print('¿Qué tipo de enemigo quieres? Existen tres categorias: 1. Enemigo ligero 2. Enemigo medio 3. Enemigo pesado')
    while True:
        enemigo = int(input('Pon el número del enemigo que desees: '))
        if 1 <= enemigo <= 3:
            break
        else:
            print('Opción inválida. Vuelva a seleccionar')
    if enemigo == 1:
        ELIGERO += 1
    elif enemigo == 2:
        EMEDIO += 1
    else:
        EPESADO += 1

def combate(dañoEnemigo, vidaEnemigo):
    global vida
    global dañoBase
    global ELIGERO
    global EMEDIO
    global EPESADO
    if ELIGERO >= 1:
        for _ in range(ELIGERO):
            vidaEnemigo = 25
            dañoEnemigo = 20
            vida -= dañoEnemigo
            vidaEnemigo -= dañoBase
            if vidaEnemigo <= 0:
                print('Has derrotado a un enemigo ligero')
            else:
                print('No has derrotado al enemigo')
    elif EMEDIO >= 1:
        for _ in range(EMEDIO):
            vidaEnemigo = 50
            dañoEnemigo = 50
            vida -= dañoEnemigo
            vidaEnemigo -= dañoBase
            if vidaEnemigo <= 0:
                print('Has derrotado a un enemigo medio')
            else:
                print('No has derrotado al enemigo')
    else:
        for _ in range(EPESADO):
            vidaEnemigo = 75
            dañoEnemigo = 80
            vida -= dañoEnemigo
            vidaEnemigo -= dañoBase
            if vidaEnemigo <= 0:
                print('Has derrotado a un enemigo pesado')
            else:
                print('No has derrotado al enemigo')

if 100 <= vida:
    print('Tu personaje tiene mucha vida')
elif 70 <= vida < 100:
    print('Tu personaje está levemente herido')
elif 50 <= vida < 70:
    print('Tu personaje está herido')
elif 0 < vida < 50:
    print('Tu personaje está gravemente herido')
else:
    print('Tu personaje está muerto')
