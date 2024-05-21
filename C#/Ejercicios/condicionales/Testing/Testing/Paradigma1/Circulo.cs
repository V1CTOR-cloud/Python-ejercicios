using System;

class Circulo : Figura
{
    public Circulo() {
        this.lados = 1;
        this.vertices = 0;
        Rodar();
    }

    public void Rodar()
    {
        Console.WriteLine("El circulo rueda 😀");
    }
}