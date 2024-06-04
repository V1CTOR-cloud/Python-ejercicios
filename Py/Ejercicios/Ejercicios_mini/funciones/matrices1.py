matriz = [
    ["J", "·", "·", "·"],
    ["·", "·", "·", "·"],
    ["·", "·", "·", "#"]          
]

#print(f"matriz", matriz)

# Imprimir columna 1
columna1 = []
for fila in matriz:
    columna1.append(fila[0])
#print(f"columna", columna1)

def Mostrar():
    for fila in matriz:
        for valor in fila:
            print("", valor, end=" ")
        print()

Mostrar()