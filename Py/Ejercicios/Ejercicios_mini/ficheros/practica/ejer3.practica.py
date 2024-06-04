nombre_fichero = input("Introduce el fichero a buscar: ")
fichero = open(nombre_fichero, "r")

i=1
arr = []
for linea in fichero:
    print(f"{i} - {linea}")
    i+=1
