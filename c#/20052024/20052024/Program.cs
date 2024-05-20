using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp7
{
    public class Clock
    {
        private int hour; //שעה 0-23
        private int min; //דקות 0-59
        public Clock(int hour, int min)
        {
            this.hour = hour;
            this.min = min;
        }
        public void GetHour(int hour) 
        {
            this.hour = hour;
        }
        public int SetHour()
        {
            return this.hour;
        }
        public void GetMin(int min)
        {
            this.min = min;
        }
        public int SetMin()
        {
            return this.min;
        }
        public int GetInterval(Clock a) 
        {
            int count = 0;
            count = a.hour*60;
            count += min;
            int day = 24*60;
            return day - count;

        }
    }

    //class Talmid
    //{
    //    private string fName;
    //    int[] grades = new int[5];
    //    double ave;
    //    public void SetFname(string fName)
    //    {
    //        this.fName = fName;
    //    }
    //    public void SetGrades(int[] grades)
    //    {
    //        this.grades = grades;
    //        ave = 0;
    //        for (int i = 0; i < grades.Length; i++)
    //            ave = ave + grades[i];
    //        ave = ave / grades.Length;
    //    }
    //    public double GetAve()
    //    {
    //        return ave;
    //    }
    //    public string GetFname()
    //    {
    //        return fName;
    //    }
    //    public int[] GetGrades()
    //    {
    //        return this.grades;
    //    }
    //}
    internal class Program
    {
        //static Random r = new Random();
        //static void ShowBest(Talmid[] k)
        //{
        //    double best = k[0].GetAve();
        //    int indexOfBest = 0;
        //    for (int i = 1; i < k.Length; i++)
        //    {
        //        if (best < k[i].GetAve())
        //        {
        //            indexOfBest = i;
        //            best = k[i].GetAve();
        //        }
        //    }
        //    int[] r = k[indexOfBest].GetGrades();
        //    for (int i = 0; i <5; i++)
        //        Console.WriteLine(r[i]);
        //    Console.WriteLine(k[indexOfBest].GetAve());
        //}
        //static void ShowKita(Talmid[] k)
        //{
        //    for (int i = 0; i < k.Length; i++)
        //    {
        //        Console.Write(k[i].GetFname() + "  ");
        //        int[] r = k[i].GetGrades();
        //        for (int q = 0; q <5; q++)
        //            Console.Write(r[q] + " ");
        //        Console.WriteLine(k[i].GetAve());
        //    }
                

        //}
        //static void kkk(Talmid[] k) 
        //{
        //    double count = 0;
        //    for (int i = 0; i < k.Length; i++)
        //        count += k[i].GetAve();
        //    count /= k.Length;
        //    int c = 0;
        //    for (int i = 0; i < k.Length; i++)
        //    {
        //        if (count < k[i].GetAve)
        //            c++;
        //    }

        //}
        static void Main(string[] args)
        {
            Console.WriteLine("hour1");
            int h1 = int.Parse(Console.ReadLine());
            Console.WriteLine("minutes1");
            int m1 = int.Parse(Console.ReadLine());
            Console.WriteLine("hour1");
            int h2 = int.Parse(Console.ReadLine());
            Console.WriteLine("minutes2");
            int m2 = int.Parse(Console.ReadLine());

            Clock a = new Clock(h1, m1);
            Console.WriteLine(a.GetInterval(a));
            Clock b = new Clock(h2, m2);
            Console.WriteLine(a.GetInterval(b));


            //Talmid[] kita = new Talmid[44];
            //for (int i = 0; i < kita.Length; i++)
            //    kita[i] = new Talmid();
            //int[] g = new int[5];
            //for (int i = 0; i < kita.Length; i++)
            //{
            //    for (int j = 0; j < 5; j++)
            //        g[j] = r.Next(0, 101);
            //    kita[i].SetGrades(g);
            //    kita[i].SetFname("RON");
            //}
            //ShowBest(kita);
            //ShowKita(kita);
        }
    }
}
