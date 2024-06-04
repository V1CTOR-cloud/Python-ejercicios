def calcular_promedio(lista):
    suma_total = sum(lista)
    promedio = suma_total / len(lista)
    return promedio

entrada_usuario = input("Ingrese una lista de números separados por comas: ")
numeros = [int(numero) for numero in entrada_usuario.split(',')]

maximo = max(numeros)
minimo = min(numeros)

suma_total = sum(numeros)

promedio = calcular_promedio(numeros)

# Mostrar los resultados
print(f"El número más grande en la lista es: {maximo}")
print(f"El número más pequeño en la lista es: {minimo}")
print(f"La suma de todos los números en la lista es: {suma_total}")
print(f"El promedio de los números en la lista es: {promedio}")