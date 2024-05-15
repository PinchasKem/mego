using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace determinanta
{
    internal class Program
    {
        static void F(int x)
        {
            if (x > 0)
            {
                if (x%2 == 0)
                    Console.WriteLine(x%10);
                F(x/10);
                if (x%2 == 1)
                    Console.WriteLine(x%10);
            }
        }
        static void ff(int x)     //  x =
        {
            if (x > 0)
            {
                for (int i = 0; i < x; i++)
                    Console.Write("{0} ", x);
                Console.WriteLine();
                ff(x-1);
                for (int i = 0; i < x; i++)
                    Console.Write("{0} ", i);
                Console.WriteLine();
            }
        }
        static void Main(string[] args)
        {
            int a= 9;
            F(a);
            ff(a);
        }
         

    }
}
