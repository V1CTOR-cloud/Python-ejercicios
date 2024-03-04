using System;

class Ejer2C
{
    static public void Exec()
    {
        // Datos del personaje
        int vida = 100;
        bool tieneArmadura = true;

        // Golpe en la cabeza (muerte instantánea)
        vida -= CalcularDanio(tieneArmadura, "Cabeza");
        Console.WriteLine("Estado del personaje después del golpe en la cabeza: " + EvaluarEstado(vida));

        // Golpe en el pecho
        vida -= CalcularDanio(tieneArmadura, "Pecho");
        Console.WriteLine("Estado del personaje después del golpe en el pecho: " + EvaluarEstado(vida));

        // Golpe en las piernas
        vida -= CalcularDanio(tieneArmadura, "Piernas");
        Console.WriteLine("Estado del personaje después del golpe en las piernas: " + EvaluarEstado(vida));

        // Golpe en los pies
        vida -= CalcularDanio(tieneArmadura, "Pies");
        Console.WriteLine("Estado del personaje después del golpe en los pies: " + EvaluarEstado(vida));
    }

    static int CalcularDanio(bool tieneArmadura, string parteCuerpo)
    {
        int danio = 0;

        switch (parteCuerpo)
        {
            case "Cabeza":
                danio = 100;
                break;
            case "Pecho":
                danio = 65;
                break;
            case "Piernas":
                danio = 25;
                break;
            case "Pies":
                danio = 10;
                break;
        }

        // Reducción de daño si tiene armadura
        if (tieneArmadura)
        {
            danio -= 10;
        }

        return danio;
    }

    static string EvaluarEstado(int vida)
    {
        if (vida > 70)
        {
            return "Intacto";
        }
        else if (vida >= 50)
        {
            return "Levemente herido";
        }
        else if (vida >= 10)
        {
            return "Herido";
        }
        else if (vida > 0)
        {
            return "Gravemente herido";
        }
        else
        {
            return "Muerto";
        }
    }
}