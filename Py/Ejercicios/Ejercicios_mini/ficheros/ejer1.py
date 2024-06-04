def contar_caracteres(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return len(content) + len(content.splitlines()) - 1

file_name = "mensaje.txt"
num_chars = contar_caracteres(file_name)
print(f"El archivo {file_name} tiene {num_chars} caracteres.")