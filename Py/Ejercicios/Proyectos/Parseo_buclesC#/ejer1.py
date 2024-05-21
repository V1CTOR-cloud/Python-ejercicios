import random

def crear_nivel(filas, columnas):
    nivel = [[" " for _ in range(columnas)] for _ in range(filas)]
    
    
    """
      A B C D E
    1 S · · · ·
    2 · · · · ·
    3 · · · · ·
    4 · · · # ·
    5 · # · · O 
    
      A B C D E
    1 S····
    2 ·····
    3 ·····
    4 ···#·
    5 ·#··O
    """
    
    nivel[0][0] = "S"
    nivel[filas-1][columnas-1] = "O"
    
    num_obstaculos = filas * columnas // 4  
    for _ in range(num_obstaculos):
        fila = random.randint(0, filas-1)
        columna = random.randint(0, columnas-1)
        nivel[fila][columna] = "#"
    
    return nivel

def imprimir_nivel(nivel):
    for fila in nivel:
        print(" ".join(fila))


filas = 5
columnas = 5

nivel = crear_nivel(filas, columnas)
imprimir_nivel(nivel)