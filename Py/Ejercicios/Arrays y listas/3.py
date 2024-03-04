def invertirLista(lista,newLista):
    for i in range(len(lista)-1,-1,-1):
        newLista.append(lista[i])
        
    newLista.append(0)
    return newLista

print(invertirLista([1,2,3,4,5], []))
print("------------------------")
print("La ciudad va a explotar")
print("------------------------")

