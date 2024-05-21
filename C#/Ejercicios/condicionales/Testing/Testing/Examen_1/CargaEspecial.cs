using System;

public class CargaEspecial : Carga
{
    public double Radioactividad { get; set; }

    public CargaEspecial(string descripcion, double peso, char categoria, double radioactividad)
        : base(descripcion, peso, categoria)
    {
        Radioactividad = radioactividad;
    }

    public override string ObtenerCaracteristicas()
    {
        return base.ObtenerCaracteristicas() + $", RADIOACTIVO: {Radioactividad}";
    }
}