using System;
using System.Collections.Generic;

class Edificio
{
    // Propiedades
    public string Techo { get; set; }
    public int Ventanas { get; set; }
    public int Puertas { get; set; }
    public string ColorExterior { get; set; }

    public string ColorInterior { get; set; }

    public List<Piso> Pisos { get; set; }

    // Constructor
    public Edificio()
    {
        ColorInterior = "verde";
        Pisos = new List<Piso>();
    }

    public void AñadirPiso(Piso piso)
    {
        Pisos.Add(piso);
    }

    public void BorrarPiso(Piso piso)
    {
        Pisos.Remove(piso);
    }
}