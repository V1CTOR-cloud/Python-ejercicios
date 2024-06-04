def mostrar_contenido_y_guardar_en_lista(file_name):
    with open(file_name, "r") as file:
        num_line = 1
        contenido_archivo = []
        max_line_lengths = []
        for line in file:
            line_length = len(line.strip())
            if len(max_line_lengths) == 0 or line_length > max_line_lengths[0]:
                max_line_lengths.insert(0, line_length)
                contenido_archivo.append(line)
            elif line_length == max_line_lengths[0]:
                contenido_archivo.append(line)
            num_line += 1
    if len(max_line_lengths) > 0:
        print(f"Las líneas más largas son:")
        for i, line in enumerate(contenido_archivo):
            print(f"{i + 1}: {line.strip()}")
    else:
        print("No se encontraron líneas en el archivo.")

mostrar_contenido_y_guardar_en_lista(input("nombre_fichero: "))