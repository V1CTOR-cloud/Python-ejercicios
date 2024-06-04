nombre_fichero = input("Introduce el fichero a buscar: ")
palabra = input("Introduce la palabra a buscar: ")
fichero = open(nombre_fichero, "r")

def buscar_palabra(palabra):
    for linea in fichero:
        if palabra in linea:
            return True
    return False

if buscar_palabra(palabra):
    print("La palabra SI existe")
else:
    print("La palabra NO existe")    