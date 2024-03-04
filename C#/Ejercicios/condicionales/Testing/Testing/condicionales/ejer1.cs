using System;

class Ejer1C
{
    static public void Exec()
    {
        bool continuar = true;

        while (continuar)
        {
            Console.WriteLine("------ MÁQUINA EXPENDEDORA ------");
            Console.WriteLine("1. Papas fritas");
            Console.WriteLine("2. Galletas");
            Console.WriteLine("3. Chocolate");
            Console.WriteLine("4. Kinder bueno");
            Console.WriteLine("5. Salir");
            Console.Write("Ingresa tu opción: ");

            int opcion = Convert.ToInt32(Console.ReadLine());

            switch (opcion)
            {
                case 1:
                    Console.WriteLine($"Has seleccionado: Papas fritas");
                    break;
                case 2:
                    Console.WriteLine($"Has seleccionado: Galletas");
                    break;
                case 3:
                    Console.WriteLine($"Has seleccionado: Chocolate");
                    break;
                case 4:
                    Console.WriteLine($"Has seleccionado: Kinder bueno");
                    break;
                case 5:
                    Console.WriteLine($"Saliendo del programa...");
                    continuar = false;
                    break;
                default:
                    Console.WriteLine($"Opción no válida. Por favor, selecciona una opción del menú.");
                    break;
            }

            Console.WriteLine();
        }
    }
}