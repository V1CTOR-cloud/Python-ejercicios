import random

def ejecutar():
    tipos_monstruos = ["Dragón", "Esqueleto", "Duende", "Gitano"]

    descripciones = [
        "Un monstruo feroz y temible que escupe fuego.",
        "Un esqueleto oscuro y misterioso que se levanta de entre los muertos.",
        "Un duende travieso que merodea por los bosques en busca de travesuras.",
        "Un gitano astuto y peligroso que conjura poderosos hechizos."
    ]

    cantidad_monstruos = int(input("Ingrese cuántos monstruos desea generar: "))

    for i in range(cantidad_monstruos):
        nombre = f"Monstruo {i + 1}"
        tipo = random.choice(tipos_monstruos)
        ataque = random.randint(10, 100)
        defensa = random.randint(5, 50)
        salud = random.randint(50, 200)
        descripcion = random.choice(descripciones)

        print(f"Monstruo {i + 1}:")
        print(f"Nombre: {nombre}")
        print(f"Tipo: {tipo}")
        print(f"Ataque: {ataque}")
        print(f"Defensa: {defensa}")
        print(f"Salud: {salud}")
        print(f"Descripción: {descripcion}")
        print()

# Se ejecuta desde func princ como C#
ejecutar()
