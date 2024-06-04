lista = [92, 87, 15, 74, 62]

def mostrar_num_grande():
    num = lista[0]
    for i in range(len(lista)):
        if lista[i] > num:
            num = lista[i]
    return num

def mostrar_num_pequenyo():
    num = lista[0]
    for i in range(len(lista)):
        if lista[i] < num:
            num = lista[i]
    return num

def calc_promedio():
    suma = 0
    
    for i in range(len(lista)):
        num = lista[i]
        suma += num
    return (suma / len(lista))


def sumar_todos():
    suma = 0
    for i in range(len(lista)):
        num = lista[i]
        suma += num
    return suma

print(mostrar_num_pequenyo())
print(mostrar_num_grande())
print(calc_promedio())
print(sumar_todos())