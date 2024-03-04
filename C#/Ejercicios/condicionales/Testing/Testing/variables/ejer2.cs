using System;

class Ejer2V
{
    static public void Exec()
    {
        // Solicitar al usuario que ingrese la información del personaje
        Console.WriteLine("¡Bienvenido al juego de rol!");
        Console.Write("Por favor, ingresa el nombre de tu personaje: ");
        string nombre = Console.ReadLine();

        Console.Write("Ingresa la salud inicial de tu personaje: ");
        int salud = Convert.ToInt32(Console.ReadLine());

        Console.Write("Ingresa el nivel de tu personaje: ");
        int nivel = Convert.ToInt32(Console.ReadLine());

        Console.Write("Ingresa la experiencia de tu personaje: ");
        int experiencia = Convert.ToInt32(Console.ReadLine());

        // Constante para la salud máxima
        const int SALUD_MAX = 100;

        // Mostrar la información del personaje
        Console.WriteLine("\nInformación del personaje:");
        Console.WriteLine("Nombre: " + nombre);
        Console.WriteLine("Salud: " + salud + "/" + SALUD_MAX);
        Console.WriteLine("Nivel: " + nivel);
        Console.WriteLine("Experiencia: " + experiencia);

        // Simular una batalla y actualizar la salud del personaje
        int danioRecibido = 20;
        salud -= danioRecibido;

        // Mostrar las estadísticas actualizadas del personaje después de la batalla
        Console.WriteLine("\nDespués de la batalla:");
        Console.WriteLine("Salud: " + salud + "/" + SALUD_MAX);
    }
}
