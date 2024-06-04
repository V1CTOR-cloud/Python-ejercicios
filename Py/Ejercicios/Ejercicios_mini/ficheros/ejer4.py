def mostrar_contenido_y_guardar_en_lista(file_name, busqueda):
    with open(file_name, "r") as file:
        num_line = 1
        contenido_archivo = []
        for line in file:
            if busqueda.lower() in line.lower():
                contenido_archivo.append(f"POS: {num_line}: {line.strip()}")
                num_line += 1
    return contenido_archivo

for elemento in mostrar_contenido_y_guardar_en_lista(input("nombre_fichero: "), input("busqueda: ")):
    print(elemento)