class Comida:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Snack(Comida):
    def __init__(self, nombre, precio, fecha_caducidad):
        super().__init__(nombre, precio)
        self.fecha_caducidad = fecha_caducidad

class Bebida(Comida):
    def __init__(self, nombre, precio, tamaño, fecha_produccion):
        super().__init__(nombre, precio)
        self.tamaño = tamaño
        self.fecha_produccion = fecha_produccion

class MaquinaExpendedora:
    def __init__(self):
        self.saldo = 0
        self.alimentos_disponibles = {
            "snacks": [Snack("Galleta", 1.5, "01/01/2023"), Snack("Patatas fritas", 2, "15/02/2023")],
            "bebidas": [Bebida("Agua", 1, "500ml", "10/01/2023"), Bebida("Refresco", 2, "330ml", "05/02/2023")]
        }
    
    def mostrar_menu(self):
        print("Bienvenido a la máquina expendedora. Su saldo actual es:", self.saldo)
        print("1. Comprar snack")
        print("2. Comprar bebida")
        print("3. Recargar saldo")
        print("4. Salir")
    
    def comprar_snack(self):
        print("Snacks disponibles:")
        for i, snack in enumerate(self.alimentos_disponibles["snacks"], start=1):
            print(f"{i}. {snack.nombre} €{snack.precio} - Fecha de caducidad: {snack.fecha_caducidad}")
        seleccion = int(input("Seleccione el número del snack que desea comprar: "))
        snack_elegido = self.alimentos_disponibles["snacks"][seleccion - 1]
        if snack_elegido.precio <= self.saldo:
            self.saldo -= snack_elegido.precio
            print(f"Ha comprado {snack_elegido.nombre}. Su saldo restante es: {self.saldo}")
        else:
            print("Saldo insuficiente.")
    
    def comprar_bebida(self):
        print("Bebidas disponibles:")
        for i, bebida in enumerate(self.alimentos_disponibles["bebidas"], start=1):
            print(f"{i}. {bebida.nombre} - {bebida.tamaño} - €{bebida.precio} - Fecha de producción: {bebida.fecha_produccion}")
        seleccion = int(input("Seleccione el número de la bebida que desea comprar: "))
        bebida_elegida = self.alimentos_disponibles["bebidas"][seleccion - 1]
        if bebida_elegida.precio <= self.saldo:
            self.saldo -= bebida_elegida.precio
            print(f"Ha comprado {bebida_elegida.nombre}. Su saldo restante es: {self.saldo}")
        else:
            print("Saldo insuficiente.")
    
    def recargar_saldo(self):
        cantidad = float(input("Introduzca la cantidad que desea recargar: "))
        self.saldo += cantidad
        print(f"Se han añadido {cantidad} al saldo. Su saldo actual es: {self.saldo}")

# Ejemplo de uso
maquina = MaquinaExpendedora()
while True:
    maquina.mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        maquina.comprar_snack()
    elif opcion == "2":
        maquina.comprar_bebida()
    elif opcion == "3":
        maquina.recargar_saldo()
    elif opcion == "4":
        print("Gracias por utilizar la máquina expendedora. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")