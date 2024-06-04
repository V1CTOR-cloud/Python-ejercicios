class Comida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Función para agregar una nueva comida al almacén
def agregar_comida(almacen):
    nombre = input("Ingrese el nombre de la comida: ")
    precio = float(input("Ingrese el precio de la comida: "))
    nueva_comida = Comida(nombre, precio)
    almacen.append(nueva_comida)
    print(f"{nombre} ha sido agregada al almacén.")

# Función para mostrar información sobre todas las comidas en el almacén
def mostrar_comidas(almacen):
    print("\nComidas en el almacén:")
    for idx, comida in enumerate(almacen, start=1):
        print(f"{idx}. Nombre: {comida.nombre}, Precio: €{comida.precio}")

# Función para actualizar una comida en el almacén
def actualizar_comida(almacen):
    mostrar_comidas(almacen)
    idx = int(input("Ingrese el número de la comida que desea actualizar: ")) - 1
    if 0 <= idx < len(almacen):
        nombre = input("Ingrese el nuevo nombre de la comida: ")
        precio = float(input("Ingrese el nuevo precio de la comida: "))
        almacen[idx].nombre = nombre
        almacen[idx].precio = precio
        print("La comida ha sido actualizada.")
    else:
        print("Índice fuera de rango. No se pudo actualizar la comida.")

# Función para eliminar una comida del almacén
def eliminar_comida(almacen):
    mostrar_comidas(almacen)
    idx = int(input("Ingrese el número de la comida que desea eliminar: ")) - 1
    if 0 <= idx < len(almacen):
        nombre_eliminado = almacen.pop(idx).nombre
        print(f"{nombre_eliminado} ha sido eliminada del almacén.")
    else:
        print("Índice fuera de rango. No se pudo eliminar la comida.")

# Almacén de comidas
almacen_comidas = []

# Menú principal
while True:
    print("\n1. Agregar comida al almacén")
    print("2. Mostrar comidas en el almacén")
    print("3. Actualizar información de una comida")
    print("4. Eliminar comida del almacén")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_comida(almacen_comidas)
    elif opcion == "2":
        mostrar_comidas(almacen_comidas)
    elif opcion == "3":
        actualizar_comida(almacen_comidas)
    elif opcion == "4":
        eliminar_comida(almacen_comidas)
    elif opcion == "5":
        print("Gracias por utilizar el sistema de gestión de almacén. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
