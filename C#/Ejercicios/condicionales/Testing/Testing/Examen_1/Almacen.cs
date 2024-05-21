using System;

public class Almacen
{
    private Carga[,] matriz;
    private int filas = 10;
    private int columnas = 20;
    private double pesoTotal = 0;

    public Almacen()
    {
        matriz = new Carga[filas, columnas];
    }

    public bool AlmacenarCarga(Carga carga)
    {
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                if (matriz[i, j] == null)
                {
                    matriz[i, j] = carga;
                    pesoTotal += carga.Peso;
                    return true;
                }
            }
        }
        return false;
    }

    public double PesoTotal => pesoTotal;

    public void OrdenarFilaPorPeso(int fila)
    {
        if (fila >= 0 && fila < filas)
        {
            Carga[] filaCargas = new Carga[columnas];
            for (int j = 0; j < columnas; j++)
            {
                filaCargas[j] = matriz[fila, j];
            }

            Array.Sort(filaCargas, (a, b) =>
            {
                if (a == null) return 1;
                if (b == null) return -1;
                return b.Peso.CompareTo(a.Peso);
            });

            for (int j = 0; j < columnas; j++)
            {
                matriz[fila, j] = filaCargas[j];
            }
        }
    }

    public double CalcularRadioactividadAcumulada()
    {
        double totalRadioactividad = 0.0;
        for (int i = 0; i < filas; i++)
        {
            for (int j = 0; j < columnas; j++)
            {
                if (matriz[i, j] is CargaEspecial cargaEspecial)
                {
                    totalRadioactividad += cargaEspecial.Radioactividad;
                }
            }
        }
        return totalRadioactividad;
    }

    public double CalcularPesoTotalPorCategoriaEnColumna(char categoria, int columna)
    {
        return CalcularPesoTotalRecursivo(categoria, columna, filas - 1);
    }

    private double CalcularPesoTotalRecursivo(char categoria, int columna, int fila)
    {
        if (fila < 0 || columna < 0 || columna >= columnas)
        {
            return 0;
        }

        double peso = 0;
        if (matriz[fila, columna] != null && matriz[fila, columna].Categoria == categoria)
        {
            peso = matriz[fila, columna].Peso;
        }

        return peso + CalcularPesoTotalRecursivo(categoria, columna, fila - 1);
    }
}