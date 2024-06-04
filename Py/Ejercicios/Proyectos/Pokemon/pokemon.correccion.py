# Manejo los errores con try catch
# Interpolaciones y tal
# Validar entradas de usuario

print("¡Oh no, el profesor Oak necesita tu ayuda, un pokémon le está atacando!")
print("Oak: Rápido, en mi bolsa hay tres pokémon, coge uno y ayúdame contra este Rattata")
print("Enfrente tuya hay tres pokéballs, elige una y a combatir")

# Datos del inicial
pokemons = {
    1: {"nombre": "Snivy", "tipo": "planta", "PS": 45, "ATAQUE": 45, "DEFENSA": 55, "ATAQUEESPECIAL": 45, "DEFENSAESPECIAL": 55, "VELOCIDAD": 63, "MOVIMIENTO1": "Placaje", "MOVIMIENTO2": "Malicioso"},
    2: {"nombre": "Piplup", "tipo": "agua", "PS": 53, "ATAQUE": 51, "DEFENSA": 53, "ATAQUEESPECIAL": 61, "DEFENSAESPECIAL": 56, "VELOCIDAD": 40, "MOVIMIENTO1": "Destructor", "MOVIMIENTO2": "Gruñido"},
    3: {"nombre": "Litten", "tipo": "fuego", "PS": 45, "ATAQUE": 65, "DEFENSA": 40, "ATAQUEESPECIAL": 60, "DEFENSAESPECIAL": 40, "VELOCIDAD": 70, "MOVIMIENTO1": "Arañazo", "MOVIMIENTO2": "Gruñido"}
}

# Datos del Rattata salvaje
rattata = {"PS": 30, "ATAQUE": 56, "DEFENSA": 35, "ATAQUEESPECIAL": 25, "DEFENSAESPECIAL": 35, "VELOCIDAD": 70, "MOVIMIENTO1": "Placaje", "MOVIMIENTO2": "Malicioso"}

bolsa = ["poción", "poción"]
equipo = []

# Elegir Pokémon
eleccionPokemon = False
while not eleccionPokemon:
    print("1. Snivy; 2. Piplup; 3. Litten")
    try:  # Try catch por aquí
        eleccion = int(input("Elige el número del pokémon que deseas: "))
        if eleccion in pokemons:
            pokemon = pokemons[eleccion]
            print(f"{pokemon['nombre']}, pokémon tipo {pokemon['tipo']}")  # Interpolación
            eleccionDefinitiva = input(f"¿Deseas elegir a {pokemon['nombre']} como tu inicial? (si/no): ").lower() # Interpolación
            if eleccionDefinitiva == "si":
                eleccionPokemon = True
                equipo.append(pokemon)
        else:
            print("Tu elección no existe")
    except ValueError:  # Si no es número falla
        print("Por favor, ingresa un número válido.")

print("Ahora que tienes tu pokemon, ¡que empiece el combate!")
print("El Rattata salvaje te corta el paso")

psRattata = rattata["PS"]
ps = pokemon["PS"]

# Combate Pokémon
while psRattata > 0 and ps > 0:
    print("Es tu turno")
    print("Menú: 1. Ataque; 2. Objetos; 3. Pokémons; 4. Huir")
    try:  # Try catch aquí
        accionTurno = int(input("¿Cuál deseas hacer? "))
        if accionTurno == 1:
            print(f"1. {pokemon['MOVIMIENTO1']}; 2. {pokemon['MOVIMIENTO2']}")  # Interpolación
            try:  # Try catch
                ataqueTurno = int(input("¿Qué ataque deseas hacer? "))
                if ataqueTurno == 1:
                    psRattata -= pokemon["ATAQUE"] * (40 / 100)
                elif ataqueTurno == 2:
                    if pokemon["MOVIMIENTO2"] == "Gruñido":
                        rattata["ATAQUE"] -= 1
                    else:
                        rattata["DEFENSA"] -= 1
                else:
                    print("Ese ataque no existe")
            except ValueError:  # Si no es núm
                print("Por favor, ingresa un número válido.")
        elif accionTurno == 2:
            print(bolsa)
            try:  # try catch
                objetoUsado = int(input("¿Cuál objeto deseas usar? "))
                if 0 < objetoUsado <= len(bolsa):
                    del bolsa[objetoUsado - 1]
                    ps += 20
                    if ps > pokemon["PS"]:
                        ps = pokemon["PS"]
                else:
                    print("No existe este objeto")
            except ValueError:  # si no es núm
                print("Por favor, ingresa un número válido.")
        elif accionTurno == 3:
            print(equipo)
            print("No tienes más pokémons")
        elif accionTurno == 4:
            print("No puedes huir")
        else:
            print("Esa acción no existe")
    except ValueError:  # si no es núm
        print("Por favor, ingresa un número válido.")

    if psRattata > 0:
        print("\nEl Rattata salvaje usó Placaje")
        ps -= rattata["ATAQUE"] * (40 / 100)
        print(f"La vida actual del Rattata es {round(psRattata)}, la vida actual de tu pokémon es {round(ps)}")  # Interpolación

if ps > 0:
    print("\nEl Rattata enemigo ha sido debilitado")
    print("Has ganado la batalla, felicidades")
    print("\nOak: Muchas gracias por haberme salvado. Veo que tú y tu pokémon estáis muy cansados")
    print("Oak: ...")
    print("Oak: Está bien, acompañadme al laboratorio")
elif psRattata > 0:
    print("Has perdido la batalla")
    print("Game Over")
