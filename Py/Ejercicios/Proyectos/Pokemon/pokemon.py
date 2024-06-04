print("¡Oh no, el profesor Oak necesita tu ayuda, un pokémon le está atacando!")
print("Oak: Rápido, en mi bolsa hay tres pokémon, coge uno y ayúdame contra este Rattata")
print("Enfrente tuya hay tres pokéballs, elige una y a combatir")
eleccionPokemon = False
bolsa=["poción","poción"]
#Datos del inicial
pokemons = {
    1: {"nombre": "Snivy", "tipo": "planta", "PS": 45, "ATAQUE": 45, "DEFENSA": 55, "ATAQUEESPECIAL": 45, "DEFENSAESPECIAL": 55, "VELOCIDAD": 63, "MOVIMIENTO1":"Placaje", "MOVIMIENTO2": "Malicioso"},
    2: {"nombre": "Piplup", "tipo": "agua", "PS": 53, "ATAQUE": 51, "DEFENSA": 53, "ATAQUEESPECIAL": 61, "DEFENSAESPECIAL": 56, "VELOCIDAD": 40, "MOVIMIENTO1":"Destructor", "MOVIMIENTO2": "Gruñido"},
    3: {"nombre": "Litten", "tipo": "fuego", "PS": 45, "ATAQUE": 65, "DEFENSA": 40, "ATAQUEESPECIAL": 60, "DEFENSAESPECIAL": 40, "VELOCIDAD": 70, "MOVIMIENTO1":"Arañazo", "MOVIMIENTO2":"Gruñido"}
}
#Datos del Rattata salvaje
rattata = {"PS": 30, "ATAQUE": 56, "DEFENSA": 35, "ATAQUEESPECIAL": 25, "DEFENSAESPECIAL": 35, "VELOCIDAD": 70, "MOVIMIENTO1":"Placaje", "MOVIMIENTO2": "Malicioso"}
equipo=[]
eleccionPokemon = False
#Elegir Pokemon
while not eleccionPokemon:
    print("1. Snivy; 2. Piplup; 3. Litten")
    eleccion = int(input("Elige el número del pokémon que deseas: "))
    if eleccion in pokemons:
        pokemon = pokemons[eleccion]
        print(f"{pokemon['nombre']}, pokémon tipo {pokemon['tipo']}")
        eleccionDefinitiva = input(f"¿Deseas elegir a {pokemon['nombre']} como tu inicial? (si/no): ").lower()
        if eleccionDefinitiva == "si":
            eleccionPokemon = True
            equipo.append(pokemon)
    else:
        print("Tu elección no existe")

print("Ahora que tienes tu pokemon, ¡que empiece el combate!")
print("El Rattata salvaje te corta el paso")

psRattata = rattata["PS"]
ps = pokemon["PS"]
#Combate Pokemon
while psRattata>0 and ps>0:
    print("Es tu turno")
    print("Menú: 1.Ataque; 2.Objetos; 3.Pokemons; 4.Huir")
    accionTurno=int(input("¿Cuál deseas hacer? "))
    if accionTurno==1:
        print("1.{0}; 2.{1}".format(pokemon["MOVIMIENTO1"], pokemon["MOVIMIENTO2"]))
        ataqueTurno=int(input("¿Qué ataque desesas hacer? "))
        if ataqueTurno==1:
            psRattata-=pokemon["ATAQUE"]*(40/100)
        elif ataqueTurno==2:
            if pokemon["MOVIMIENTO2"]=="Gruñido":
                rattata["ATAQUE"]-=1
            else:
                rattata["DEFENSA"]-=1
        else:
            print("Ese ataque no existe")
    if accionTurno==2:
        print(bolsa)
        objetoUsado=int(input("¿Cuál objeto deseas usar? "))
        if 0<objetoUsado<(len(bolsa)+1):
            del bolsa[objetoUsado-1]
            ps+=20
            if ps>pokemon["PS"]:
                ps=pokemon["PS"]
        else:
            print("No existe este objeto")
    elif accionTurno==3:
        print(equipo)
        print("No tienes más pokemons")
    elif accionTurno==4:
        print("No puedes huir")
    if psRattata>0:
        print()
        print("El Rattata salvaje usó placaje")
        ps-=rattata["ATAQUE"]*(40/100)
        print("\nLa vida actual del Rattata es {0}, la vida actual de tu pokemon es {1}".format(round(psRattata), round(ps)))

#Acaba el combate
if ps>0:
    print("\nEl rattata enemigo ha sido debilitado")
    print("Has ganado la batalla, felicidades")
    print("\nOak: Muchas gracias por haberme salvado. Veo que tú y tu pokemon estáis muy cansados")
    print("Oak: ...")
    print("Oak: Está bien acompañadme al laboratorio")
elif psRattata>0:
    print("Has perdido la batalla")
    print("Game Over")