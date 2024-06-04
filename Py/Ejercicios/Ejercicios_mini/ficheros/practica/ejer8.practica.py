nombre_fichero = input("Introduce el fichero a buscar: ")
fichero = open(nombre_fichero, "r")

i=0

for linea in fichero:
    if i < 10:
        print(linea)
        i+=1