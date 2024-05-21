using System;

class Examen_ejer1
{
    static public void Exec()
    {
        Almacen almacen = new Almacen();

        almacen.AlmacenarCarga(new Carga("Muestras planeta Zhyron", 320, 'Y'));
        almacen.AlmacenarCarga(new CargaEspecial("Material nuclear", 500, 'X', 15.3));
        almacen.AlmacenarCarga(new Carga("Herramientas", 150, 'Z'));

        Console.WriteLine("Radioactividad acumulada: " + almacen.CalcularRadioactividadAcumulada());

        Console.WriteLine("Peso total de categoría 'Y' en columna 0: " + almacen.CalcularPesoTotalPorCategoriaEnColumna('Y', 0));

        almacen.OrdenarFilaPorPeso(0);
    }
}
