using System;

class Ejer1B
{
    static public void Exec()
    {
        // Tamaño del nivel
        int filas = 10;
        int columnas = 10;

        // Matriz para representar el nivel
        char[,] nivel = new char[filas, columnas];

        // Inicializar nivel con espacios vacíos
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                nivel[i, j] = '.';
            }
        }

        // Posicionar jugador en la esquina superior izquierda
        nivel[0, 0] = 'S';

        // Posicionar objetivo en la esquina inferior derecha
        nivel[filas - 1, columnas - 1] = 'O';

        // Generar obstáculos aleatorios
        Random rnd = new Random();
        for (int i = 0; i < filas * columnas / 3; i++) // Aproximadamente un tercio de la matriz será obstáculos
        {
            int filaObstaculo = rnd.Next(0, filas);
            int columnaObstaculo = rnd.Next(0, columnas);
            nivel[filaObstaculo, columnaObstaculo] = '#';
        }

        // Imprimir nivel generado
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                Console.Write(nivel[i, j] + " ");
            }
            Console.WriteLine();
        }
    }
}
