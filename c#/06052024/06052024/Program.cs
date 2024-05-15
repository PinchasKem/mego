using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _06052024
{
    internal class Program
    {
        static void A(int a)
            if(a>9)
             {
            a=a%10;
            A(a);
            }
        static bool F(int[] a)
        {
            if (a.Length%2 == 1)
                return false;
            int count = 0;
            for (int i = 0; i < a.Length; i++)
            {                    
                if(a[i] == 0)
                    return false;
                if (a[i] > 0)
                    count++;
            if(count == a.Length/2)
                    return true;
            return false;
            }
        }
        public static void What(int[] arr, int num)
        {
            int left = 0;
            int right = arr.Length-1;
            while (left!=right)
            {
                if (arr[left] < num)
                    left++;
                else
                if (arr[right] > num)
                    right--;
                else
                {
                    int temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = temp;
                }
            }
        }
        static void Main(string[] args)
        {
        }
    }
}
