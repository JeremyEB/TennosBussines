/*Importamos estas funciones de C#*/
using System;
using System.Collections.Generic;

/*Creamos la clase del programa*/
class Program
{
    /*Creamos primero esta funcion donde agregaremos los valores al array*/
    static void Main(string[] args)
    {
        /*Array uno agregamos su valores*/
        int[] array1 = { 1, 2, 3, 4, 5 };
        /*Array dos agregmos sus valores*/
        int[] array2 = { 2, 4 };
        /*Array 3 sera igual a los valores removidos con la funcion ValoresLimpios*/
        int[] arraySinDuplicados = ValoresLimpios(array1, array2);
        /*Imprimimos por consola el array3*/
        Console.WriteLine("Valores no repetidos: " + string.Join(", ", arraySinDuplicados));
    }
    /*Creamos la funcion ValoresLimpios coon los parrametros de los array agregados*/
    public static int[] ValoresLimpios(int[] array1, int[] array2)
    {
        /*Usamos la funcion HashSet que nos ayuda a evitar que los valores se dupliquen*/
        HashSet<int> set = new HashSet<int>(array2);
        /*Creamos una variable que almacenara una lista*/
        List<int> arraySinDuplicados = new List<int>();
        /*Y con el bucle ForEach se recorrera el primera array y comprobara si un digito se encuentra
         en la variable set que es donde se almacena los valoers que no estan duplicados*/
        foreach (int num in array1)
        {
            if (!set.Contains(num))
            {
                arraySinDuplicados.Add(num);
            }
        }
        /*Y al final tenemos nuestra array sin duplicados*/
        return arraySinDuplicados.ToArray();
    }
}