# Menú por consola
print("Bienvenido al menú de snacks:")
print("1. Papas fritas")
print("2. Galletas")
print("3. Chocolate")
print("4. kinder bueno blanco")
print("5. Salir")

# Lectura de la opción 
opcion = int(input("Ingresa el número de la opción que deseas: "))


# Comparación múltiple y mostrado del producto
if opcion == 1:
    print("Has elegido papas fritas.")
elif opcion == 2:
    print("Has elegido galletas.")
elif opcion == 3:
    print("Has elegido chocolate.")
elif opcion == 4:
    print("Has elegido kinder bueno blanco.")
elif opcion == 5:
    print("¡Hasta luego!")
else:
    print("Opción no válida. Por favor, elige una opción del menú.")