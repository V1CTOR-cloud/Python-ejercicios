using System;

class Examen_ejer2
{
    static public void Exec()
    {
        Almacen almacen = new Almacen();
        Random random = new Random();
        char[] categorias = { 'X', 'Y', 'Z' };

        while (almacen.PesoTotal <= 40000)
        {
            string descripcion = $"Muestras del planeta #{almacen.PesoTotal}";
            double peso = random.Next(50, 351);
            char categoria = categorias[random.Next(categorias.Length)];

            if (random.Next(2) == 0) // 50% probabilidad de ser CargaEspecial
            {
                double radioactividad = random.NextDouble() * (20 - 5) + 5;
                CargaEspecial cargaEspecial = new CargaEspecial(descripcion, peso, categoria, radioactividad);
                if (!almacen.AlmacenarCarga(cargaEspecial)) break;
            }
            else
            {
                Carga carga = new Carga(descripcion, peso, categoria);
                if (!almacen.AlmacenarCarga(carga)) break;
            }
        }

        Console.WriteLine("Radioactividad acumulada: " + almacen.CalcularRadioactividadAcumulada());
    }
}