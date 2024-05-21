using System;

class Ejer2B
{
    static public void Exec()
    {
        // Tipos de monstruos disponibles
        string[] tiposMonstruos = { "Dragón", "Esqueleto", "Duende", "Gitano" };

        // Descripciones aleatorias para los monstruos
        string[] descripciones = {
            "Un monstruo feroz y temible que escupe fuego.",
            "Un esqueleto oscuro y misterioso que se levanta de entre los muertos.",
            "Un duende travieso que merodea por los bosques en busca de travesuras.",
            "Un gitano astuto y peligroso que conjura poderosos hechizos."
        };

        // Solicitar al usuario la cantidad de monstruos a generar
        Console.Write("Ingrese cuántos monstruos desea generar: ");
        int cantidadMonstruos = int.Parse(Console.ReadLine());

        // Generar y mostrar descripción para cada monstruo
        for (int i = 0; i < cantidadMonstruos; i++)
        {
            // Generar aleatoriamente características del monstruo
            Random rnd = new Random();
            string nombre = "Monstruo " + (i + 1);
            string tipo = tiposMonstruos[rnd.Next(tiposMonstruos.Length)];
            int ataque = rnd.Next(10, 101);
            int defensa = rnd.Next(5, 51);
            int salud = rnd.Next(50, 201);
            string descripcion = descripciones[rnd.Next(descripciones.Length)];

            // Mostrar la descripción del monstruo generado
            Console.WriteLine($"Monstruo {i + 1}:"); 
            Console.WriteLine($"Nombre: {nombre}");
            Console.WriteLine($"Tipo: {tipo}");
            Console.WriteLine($"Ataque: {ataque}");
            Console.WriteLine($"Defensa: {defensa}");
            Console.WriteLine($"Salud: {salud}");
            Console.WriteLine($"Descripción: {descripcion}");
            Console.WriteLine();
        }
    }
}
