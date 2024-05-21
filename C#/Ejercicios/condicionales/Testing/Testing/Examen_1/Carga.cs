using System;

public class Carga
{
    public string Descripcion { get; }
    public double Peso { get; }
    public char Categoria { get; }

    public Carga(string descripcion, double peso, char categoria)
    {
        Descripcion = descripcion;
        Peso = peso;
        Categoria = categoria;
    }

    public virtual string ObtenerCaracteristicas()
    {
        return $"Carga: {Descripcion}, Peso: {Peso} Kg, Categoría: {Categoria}";
    }
}