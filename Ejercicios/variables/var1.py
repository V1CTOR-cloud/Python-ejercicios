# Solicitar al usuario que ingrese el daño base, nivel del personaje y bonificación
DAÑO_BASE = 25
nivel_personaje = int(input("Por favor, ingrese el nivel del personaje: "))
bonificacion = float(input("Por favor, ingrese la bonificación del personaje: "))

# Operación con el PA
pa = (DAÑO_BASE + nivel_personaje) * bonificacion

# Mostramos el resultado
print("El Poder de Ataque (PA) del personaje es:", pa)