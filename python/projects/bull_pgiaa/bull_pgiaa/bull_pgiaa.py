import sys
import random
from colorama import Fore, Back, Style ,init
init(autoreset=True)

def main():
    print(Fore.YELLOW+("    " + '-'*15))
    print(Fore.YELLOW+("   | 1 | 2 | 3 | 4 |"))
    print(Fore.YELLOW+("    " + '-'*15))

def colors():
    print("   "+\
          A + "=1    " +\
          D + "=4  \n" +\
          "   " + B + "=2    " +\
          E + "=5  \n" +\
          "   " + C + "=3    " +\
          F + "=6")

def to_choose():
    success = 0
    attempts = 0
    while(success == 0):
        choice = [0 for _ in range(4)]           
        display(choice)
        i = 0
        while(i < 4):
            colors()
            choice[i] = int(input("Choose a color for " + str(i+1) + ": "))
            sys.stdout.write("\033[F\033[F\033[F\033[F")  
            sys.stdout.write("\033[K\033[K\033[K\033[K")   
            if(choice[i] < 7  and  choice[i] > 0):
                sys.stdout.write("\033[F\033[F\033[F")  
                sys.stdout.write("\033[K\033[K\033[K")
                display(choice)
                i += 1       
        Counter1 = 0
        Counter2 = 0
        b = a.copy()
        for i in range(4):
            if(choice[i] == b[i]):
                b[i] = 0
                choice[i] = -1
                Counter1 += 1
        for i in range(4):
            for j in range(4):
                if(choice[i] == b[j]):
                    b[j] = 0
                    choice[i] = -1
                    Counter2 += 1
        print('        ' + G*Counter2 + '  ' + F*Counter1)
        attempts += 1
        if(Counter1 == 4):
            print("  " , "$" * 17 , "\n    You succeeded in" , str(attempts) , "attempts")
            success = 1 
   
def display(choice):
    print("    " + '-'*15 + '      ' + "\n  ", end="") 
    for i in range(4):
        print(" | " + str(eindex[choice[i]]) , end="")
    print(' |' + "\n    " + '-'*15 + '      ')
    
####    MAIN    ####

A = Fore.YELLOW + "\u25CF"
B = Fore.BLUE   + "\u25CF" 
C = Fore.GREEN  + "\u25CF" 
D = Fore.RED + "\u25CF" 
E = Fore.LIGHTMAGENTA_EX + "\u25CF" 
F = Fore.WHITE + "\u25CF" 
G = Fore.WHITE + "\u25CB"
eindex = [' ', A, B, C, D, E, F]

a = [0 for _ in range(4)]
for i in range(4):
    a[i] = random.randint(1,6)
main()
to_choose() 