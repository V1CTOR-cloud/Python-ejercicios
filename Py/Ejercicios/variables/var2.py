# Experiencia de los enemigos
XP_LIGERO = 5
XP_MEDIO = 10
XP_PESADO = 30

# Nivel del j
nivel = int(input("ingresa el nivel del jugador: "))

# Multiplicador de nivel (suponiendo un 10% de reducción por nivel)
multiplicador_nivel = (1 - nivel * 0.1)

# Calcular la experiencia total
XP_TOTAL = (XP_LIGERO + XP_MEDIO + XP_PESADO) * multiplicador_nivel

# Evita los nums negativos
XP_TOTAL = max(XP_TOTAL, 1)

# Mostrar el resultado
print("La experiencia total obtenida al matar a los enemigos es:", XP_TOTAL)