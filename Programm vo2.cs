using System;

namespace Beispiel
{
    class Programm
    {
        const int ZielZahl = 5;

        static void Main(string[] args)
        {
            int zahl = 5;
            �berpr�feZahlUndGibAus(zahl);
        }

        static void �berpr�feZahlUndGibAus(int zahl)
        {
            if (zahl == ZielZahl)
            {
                Console.WriteLine($"Die Zahl ist {ZielZahl}.");
            }
        }
    }
}
