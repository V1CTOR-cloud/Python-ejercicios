class Program
{
    static private void Main()
    {
        // Llamar al método Exec()
        // Variables
        //Ejer1V.Exec();
        //Ejer2V.Exec();

        // Condicionales
        //Ejer1C.Exec();
        //Ejer2C.Exec();

        //Bucles
        //Ejer1B.Exec();
        //Ejer2B.Exec();
        //Ejer1CYB.Exec();
        //Examen_ejer1.Exec();
        //Examen_ejer2.Exec();


        //Circulo circulo = new Circulo();
        //Triangulo triangulo = new Triangulo();

        //Repeticiones(triangulo.lados);

        //Pentagono pentagono = new Pentagono();
        //Repeticiones(pentagono.lados);

        //Decaedro decaedro = new Decaedro();
        //Repeticiones(decaedro.lados);

        //int numeroInicio = 10;
        //ContadorParesAtras(numeroInicio);

        Duendes[] duendes = new Duendes[10];



    }

    public static void Repeticiones(int lados)
    {
        for (int i = 1; i < lados; i++)
        {
            switch (lados)
            {
                case 3:
                    Triangulo triangulo = new Triangulo();
                    break;

                case 5:
                    Pentagono pentagono = new Pentagono();
                    break;

                case 10:
                    Decaedro decaedro = new Decaedro();
                    break;
            }
        }
    }

    public static void ContadorAtras(int contador)
    {
        if (contador < 0) return;
        Console.WriteLine(contador);
        ContadorAtras(contador - 1);
    }

    public static void ContadorParesAtras(int contador)
    {
        if(contador < 0) return;
        if (contador % 2 == 0) Console.WriteLine(contador);
        ContadorParesAtras(contador - 1);
    }

    public static void AsignarRevoltosos(int contador, Duendes[] duendes)
    {
        if (contador < 0) return;
        if (contador % 2 == 0) duendes[contador].esRevoltoso = true;
        AsignarRevoltosos(contador, duendes);
    }
}
