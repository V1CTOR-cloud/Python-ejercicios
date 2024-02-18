def mostrar_inventario(inventario):
    print("Inventario actual:")
    for i, item in enumerate(inventario, start=1):
        calidad, tipo = inventario[item]
        print(f"{i}. {item}: Calidad {calidad}, Tipo {tipo}")

def actualizar_inventario(inventario, item_nuevo, calidad_nuevo, tipo_nuevo):
    if len(inventario) < 15:
        inventario[item_nuevo] = (calidad_nuevo, tipo_nuevo)
        print(f"Se ha añadido '{item_nuevo}' al inventario.")
    else:
        print("¡El inventario está lleno! No se puede añadir más items.")

def cambiar_item(inventario, indice_cambio, item_nuevo, calidad_nuevo, tipo_nuevo):
    if 1 <= indice_cambio <= len(inventario):
        item_antiguo = list(inventario.keys())[indice_cambio - 1]
        inventario[item_nuevo] = (calidad_nuevo, tipo_nuevo)
        del inventario[item_antiguo]
        print(f"Se ha cambiado '{item_antiguo}' por '{item_nuevo}' en el inventario.")
    else:
        print("Índice de inventario inválido.")

# Inventario inicial del jugador
inventario_jugador = {
    "espada": (80, "arma"),
    "pociones": (10, "consumible"),
    "armadura": (70, "equipo"),
    "amuleto": (90, "accesorio"),
    "botas": (75, "equipo")
}

print("¡Bienvenido al juego!")

while True:
    opcion = input("¿Deseas encontrar un nuevo item? (s/n): ").lower()
    
    if opcion == 'n':
        print("Fin del juego.")
        break
    
    elif opcion == 's':
        # Simulación de encontrar un nuevo item
        item_nuevo = input("Introduce el nombre del nuevo item: ")
        calidad_nuevo = int(input("Introduce la calidad del nuevo item (0-100): "))
        tipo_nuevo = input("Introduce el tipo del nuevo item: ")
        
        mostrar_inventario(inventario_jugador)
        
        decision = input("¿Deseas cambiar este item por uno de tu inventario? (s/n): ").lower()
        if decision == 's':
            indice_cambio = int(input("Introduce el número del item que deseas cambiar: "))
            cambiar_item(inventario_jugador, indice_cambio, item_nuevo, calidad_nuevo, tipo_nuevo)
        else:
            actualizar_inventario(inventario_jugador, item_nuevo, calidad_nuevo, tipo_nuevo)
        
        mostrar_inventario(inventario_jugador)
        
    else:
        print("Opción no válida. Por favor, introduce 's' para sí o 'n' para no.")
