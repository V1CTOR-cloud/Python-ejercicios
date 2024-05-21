using System;

class Triangulo : Figura
{
    public Triangulo()
    {
        this.vertices = 3;
        this.lados = 3;
        Nada();
    }

    public void Nada()
    {
        Console.WriteLine("El triangulo no hace nada ☹");
    }
}