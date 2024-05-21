using System;

class Almacen1
{
    private Carga1[,] matriz;
    private int filas = 10;
    private int columnas = 20;

    public Almacen1() {
        this.matriz = new Carga1[filas, columnas];

        /* * * * * *
         * * * * * *
         * * * * * *
         * * * * * *
         * * * * * *
         */

        // 
    }

    public bool AlmacenarCarga(Carga1 carga)
    {
        for (int fila = 0; fila < this.filas; fila++)
        {
            for (int columna = 0; columna < this.columnas; columna++)
            {
                if (matriz[fila,columna] == null)
                {
                    matriz[fila,columna] = carga;
                    return true;
                }
            }
        }
        return false;
    }

    
}
