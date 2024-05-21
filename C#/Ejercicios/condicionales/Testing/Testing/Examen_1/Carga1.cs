using System;

class Carga1
{
    public string Descripcion { get; }
    public int Peso { get; }
    public char Categoria { get; }

    public Carga1(string NewDescripcion, int newPeso, char newCategoria)
    {
        this.Descripcion = NewDescripcion;
        this.Peso = newPeso;

        switch (newCategoria)
        {
            case 'X':
                this.Categoria = newCategoria;
                break;
            case 'Y':
                this.Categoria = newCategoria;
                break;
            case 'Z':
                this.Categoria = newCategoria;
                break;

            default:
                Console.WriteLine("Error, la categoría no coincide");
                break;
        }
    }

    public virtual void MostrarCaracteristicas()
    {
        Console.WriteLine($"Descripción: {this.Descripcion}");
        Console.WriteLine($"Peso: {this.Peso}");
        Console.WriteLine($"Categoría: {this.Categoria}");
    }

    public string getDescripcion()
    {
        return this.Descripcion;
    }
}