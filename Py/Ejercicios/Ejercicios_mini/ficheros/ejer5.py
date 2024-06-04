def mostrar_contenido_y_guardar_en_lista(file_name):
    with open(file_name, "r") as file:
        num_line = 1
        contenido_archivo = []
        max_line_length = 0
        max_line = ""
        for line in file:
            if len(line.strip()) > max_line_length:
                max_line_length = len(line.strip())
                max_line = line.strip()
            contenido_archivo.append(f"{num_line}: {line.strip()}")
            num_line += 1
    print(max_line)

mostrar_contenido_y_guardar_en_lista(input("nombre_fichero: "))