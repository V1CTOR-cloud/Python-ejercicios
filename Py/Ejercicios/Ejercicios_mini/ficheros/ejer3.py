def mostrar_contenido(file_name):
    with open(file_name, "r") as file:
        num_line = 1
        for line in file:
            print(f"{num_line}: {line.strip()}")
            num_line += 1

mostrar_contenido(input("nombre_fichero: "))