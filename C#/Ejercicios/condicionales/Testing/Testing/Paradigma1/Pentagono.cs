using System;

class Pentagono : Figura
{
    public Pentagono()
    {
        this.vertices = 5;
        this.lados = 5;
        Nada();
    }

    public void Nada()
    {
        Console.WriteLine("El Pentagono no hace nada ☹");
    }
}