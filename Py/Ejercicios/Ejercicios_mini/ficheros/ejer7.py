def head(file_name, num_lines):
    with open(file_name, "r") as file:
        head_lines = [line.strip() for line in file.readlines()[:num_lines]]
    for line in head_lines:
        print(line)

head(input("Archivo: "), 10)