def busca_palabra(file_name, word):
    with open(file_name, "r") as file:
        for line in file:
            if word in line:
                print("Existe")

file_name = "mensaje.txt"
word = input("Que palabra deseas buscar: ")
busca_palabra(file_name, word)