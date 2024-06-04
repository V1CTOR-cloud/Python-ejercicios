nombre_fichero = input("Introduce el fichero a buscar: ")
fichero = open(nombre_fichero, "r")

contador = 0
a=0
for linea in fichero:
    a+=1
    for caracter in linea:
        contador += 1
    
a -=1    
print(contador+a)