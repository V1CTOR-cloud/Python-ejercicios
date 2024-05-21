using System;

class Decaedro : Figura
{
    public Decaedro()
    {
        this.vertices = 10;
        this.lados = 10;
        Nada();
    }

    public void Nada()
    {
        Console.WriteLine("El decaedro no hace nada ☹");
    }
}