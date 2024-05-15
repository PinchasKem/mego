using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _13052024
{
    internal class Program
    {
        static int f(int x)
        {
            if (x>0)
                if (x%2==0)
                    return 1 + f(x/10);
                else
                    return f(x/10);
            return 0;
        }
        static int ff(int x)
        {
            if (x>0)
            {
                if (x%2 == 0)
                {
                    return x%10 + ff(x/10);
                }
                else
                {
                    return ff(x/10) - x%10;
                }
            }
            return 0;
        }

        static void FFF(int x)
        {
            if (x>0)
            {
                if (x%2 == 0)
                {
                    for (int i = x%)
                    Console.WriteLine(x%10);
                }
                FFF(x/10);
                if (x%2 == 1)
                {
                    Console.WriteLine(x%10);
                }
            }
        }


        static void Main(string[] args)
        {
            int x = 456328895;
            //Console.WriteLine(FFF(x));
            FFF(x);
        }
    }
}
