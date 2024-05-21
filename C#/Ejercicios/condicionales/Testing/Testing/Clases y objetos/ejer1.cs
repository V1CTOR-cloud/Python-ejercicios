using System;

class Ejer2CYB
{
    static public void Exec()
    {
        // Crear la casa 1
        Edificio casa_1 = new Edificio();
        casa_1.Techo = "Teja";
        casa_1.Ventanas = 3;
        casa_1.Puertas = 1;
        casa_1.ColorExterior = "Azul";
        casa_1.ColorInterior = "Blanco";

        Edificio casa_3 = new Edificio();
        casa_3.Techo = "Tungsteno";
        casa_3.Puertas = 1;
        casa_3.ColorExterior = "Gris";
        casa_3.ColorInterior = "Blanco huevo";

        
        for (int i = 1; i < 21; i++) // 20 pisos
        {
            Piso newPiso = new Piso();


            if (i % 2 == 0) newPiso.tieneMoqueta = false;
            else newPiso.sePermiteAnimales = true;

            casa_3.AñadirPiso(newPiso);
            casa_3.Ventanas += 5;
        }


        Console.WriteLine(casa_1.Techo); // Teja
    }
}