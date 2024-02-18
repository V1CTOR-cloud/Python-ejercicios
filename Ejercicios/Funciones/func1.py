def calcular_experiencia(nivel_jugador, dificultad_enemigo):
    # Definir la cantidad base de puntos de experiencia
    puntos_base = 100
    
    # Ajustar la cantidad de puntos de experiencia según el nivel del jugador y la dificultad
    multiplicador_nivel = nivel_jugador / 10  # Ejemplo: cada 10 niveles aumenta el multiplicador
    if dificultad_enemigo == "fácil":
        puntos_extra = 50 * multiplicador_nivel
    elif dificultad_enemigo == "media":
        puntos_extra = 100 * multiplicador_nivel
    elif dificultad_enemigo == "difícil":
        puntos_extra = 150 * multiplicador_nivel
    elif dificultad_enemigo == "nightmare":
        puntos_extra = 200 * multiplicador_nivel
    else:
        print("Dificultad no reconocida.")
        return 0
    
    # Calcular la experiencia total
    experiencia_total = puntos_base + puntos_extra
    
    return experiencia_total

# Ejemplo de uso
nivel = 10
dificultad = "nightmare"

experiencia_ganada = calcular_experiencia(nivel, dificultad)
print(f"El jugador de nivel {nivel} ganó {experiencia_ganada} puntos de experiencia al derrotar a un enemigo de dificultad {dificultad}.")
