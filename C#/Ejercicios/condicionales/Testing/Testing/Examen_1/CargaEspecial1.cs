using System;
class CargaEspecial1 : Carga1
{
    public int Radioactivo {  get; set; }

    public CargaEspecial1(string NewDescripcion, int newPeso, char newCategoria, int radioactivo) : base(NewDescripcion, newPeso, newCategoria)
    {
        Radioactivo = radioactivo;
    }

    public override void MostrarCaracteristicas()
    {
        base.MostrarCaracteristicas();
        Console.WriteLine($" RADIOACTIVO: {this.Radioactivo}");
    }
}
