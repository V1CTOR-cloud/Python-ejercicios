
using System;
using System.Collections.Generic;

class Piso
{
    // Propiedades
    public bool tieneMoqueta { get; set; }
    public string colorMoqueta { get; set; }
    public int cantidadMuebles { get; set; }
    public bool sePermiteAnimales { get; set; }

    // Constructor
    public Piso()
    {
        sePermiteAnimales = false;
        colorMoqueta = "Negro";
    }

}