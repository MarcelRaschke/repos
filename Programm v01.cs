using System;
using System.Collections.Generic;

namespace Beispiel
{
    class Programm
    {
        const int ZielZahl = 5;

        static void Main(string[] args)
        {
            List<int> zahlen = new List<int> { 3, 5, 7, 5, 9 };
            �berpr�feZahlenUndGibAus(zahlen);
        }

        static void �berpr�feZahlenUndGibAus(List<int> zahlen)
        {
            foreach (int zahl in zahlen)
            {
                �berpr�feZahlUndGibAus(zahl);
            }
        }

        static void �berpr�feZahlUndGibAus(int zahl)
        {
            if (zahl == ZielZahl)
            {
                Console.WriteLine($"Die Zahl ist {ZielZahl}.");
            }
            else
            {
                Console.WriteLine($"Die Zahl ist nicht {ZielZahl}.");
            }
        }
    }
}
