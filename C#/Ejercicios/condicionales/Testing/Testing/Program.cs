class Program
{
    static private void Main()
    {
        // Llamar al método Exec()
        // Variables
        //Ejer1V.Exec();
        //Ejer2V.Exec();

        // Condicionales
        //Ejer1C.Exec();
        //Ejer2C.Exec();


        Console.WriteLine("Nombre: (Gustavo) ");
        Console.WriteLine("Salud: (100) ");
        int salud = Int32.Parse(Console.ReadLine());
        Console.WriteLine("Nivel: (5) ");
        Console.WriteLine("Experiencia: (0) ");
        Console.WriteLine("Salud máxima: (100) ");
        const int SALUD_MAX = 100;

        salud -= 20;

        Console.WriteLine(salud);
    }
}
