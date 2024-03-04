# Personaje
vida = 100
armadura = False

# función para recibir daño y evuluar daños 
def recibir_danio(tipo_danio):
    global vida
    danio_efectivo = 0
    if tipo_danio == "Cabeza":
        vida = 0
        danio_efectivo = 100
    elif tipo_danio == "Pecho":
        danio_efectivo = 65
    elif tipo_danio == "Piernas":
        danio_efectivo = 25
    elif tipo_danio == "Pies":
        danio_efectivo = 10
    
    if armadura:
        danio_efectivo = max(0, danio_efectivo - 10)
        
    vida -= danio_efectivo
    print(f"El personaje recibe {danio_efectivo} puntos de daño en {tipo_danio}.")

# Aplicar daño en diferentes partes del cuerpo
recibir_danio("Cabeza")  # Golpe en la cabeza
recibir_danio("Pecho")   # Golpe en el pecho
recibir_danio("Piernas") # Golpe en las piernas
recibir_danio("Pies")    # Golpe en los pies

# Evaluar el estado del personaje
if vida == 100:
    print("El personaje está intacto.")
elif 70 <= vida:
    print("El personaje está levemente herido.")
elif 50 <= vida < 70:
    print("El personaje está herido.")
elif 10 <= vida < 50:
    print("El personaje está gravemente herido.")
elif vida <= 0:
    print("El personaje está muerto.")