using System;
using System.Collections.Generic;
using System.Linq;

namespace Beispiel
{
    class Programm
    {
        const int ZielZahl = 5;

        static void Main(string[] args)
        {
            Console.WriteLine("Geben Sie eine Liste von Zahlen ein, getrennt durch Kommas:");
            string eingabe = Console.ReadLine();
            List<int> zahlen = ParseZahlen(eingabe);
            �berpr�feZahlenUndGibAus(zahlen);
        }

        static List<int> ParseZahlen(string eingabe)
        {
            return eingabe.Split(',')
                          .Select(z => int.TryParse(z.Trim(), out int zahl) ? zahl : (int?)null)
                          .Where(z => z.HasValue)
                          .Select(z => z.Value)
                          .ToList();
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

