archivo = open("mensaje.txt", "r")
print(archivo.read())
print(archivo.readline())
print(archivo.read(5))

for linea in archivo:
  print(linea)