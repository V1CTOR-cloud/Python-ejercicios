using System;

class Ejer1V
{
    static public void Exec()
    {
        // Generar un objeto de tipo Random para simular el lanzamiento del dado
        Random random = new Random();

        // Definir una variable para almacenar el resultado del lanzamiento del dado
        int resultadoDado;

        // Mensaje de bienvenida
        Console.WriteLine("!Bienvenido al Simulador de Lanzamiento de Dado!");

        // Bucle para permitir m�ltiples lanzamientos del dado
        while (true)
        {
            // Pedir al usuario que presione una tecla para lanzar el dado
            Console.WriteLine("\nPresiona cualquier tecla para lanzar el dado...");
            Console.ReadKey(true);

            // Generar un n�mero aleatorio entre 1 y 6 para simular el lanzamiento del dado
            resultadoDado = random.Next(1, 7);

            // Mostrar el resultado del lanzamiento del dado
            Console.WriteLine("!Has obtenido un " + resultadoDado + "!\n");

            // Preguntar al usuario si desea lanzar el dado nuevamente
            Console.Write("!Quieres lanzar el dado nuevamente? (s/n): ");
            char respuesta = Console.ReadKey(true).KeyChar;

            // Salir del bucle si el usuario no quiere lanzar el dado nuevamente
            if (respuesta != 's' && respuesta != 'S')
            {
                Console.WriteLine("\n\n!Gracias por jugar!");
                break;
            }
        }
    }
}