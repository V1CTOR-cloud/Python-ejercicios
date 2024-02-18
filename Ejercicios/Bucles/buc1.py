altura = int(input("Introduce la altura de la pirámide: "))
caracter = input("Introduce el carácter que deseas usar para construir la pirámide: ")

for i in range(altura):
    print(' ' * (altura - i - 1) + caracter * (2 * i + 1))