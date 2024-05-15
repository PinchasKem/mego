from ast import Global
from colorama import Fore, Back, Style ,init
init(autoreset=True)

def display():
    print('    ','-'*39)
    q = [ 0 , '|' +Fore.RED +  ' O  ' , '|' +Fore.GREEN +  ' X  ']
    for i in range(8):
        print('    ', end = '')
        for j in range(8): 
            if((i*8+j+1) < 10):
                q[0] = F'| {i*8+j+1}  ' 
            else:
                q[0] = F'| {i*8+j+1} '
            print(q[a[i][j]], end = '')   
        print('|')
        print('    ','-'*39)

## 
def Is_there(player):
    for i in range(8):
        for j in range(8):
            if(a[i][j] == 0):
                opponent = 1 if player == 2 else 2
                directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]   ## 
                for i2, j2 in directions:
                    i3, j3 = i + i2, j + j2
                    if (-1 < i3 < 8) and (-1 < j3 < 8) and a[i3][j3] == opponent:
                        while (-1 < i3 < 8) and (-1 < j3 < 8) and a[i3][j3] == opponent:
                            i3, j3 = i3 + i2, j3 + j2
                        if (-1 < i3 < 8) and (-1 < j3 < 8) and a[i3][j3] == player:
                            return True
    return False        

##  
def is_valid_move(player):
    if(a[i1][j1] > 0):               ## 
        return False
    opponent = 1 if player == 2 else 2
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]   ## 
    for i2, j2 in directions:
        i, j = i1 + i2, j1 + j2
        if (-1 < i < 8) and (-1 < j < 8) and a[i][j] == opponent:
            while (-1 < i < 8) and (-1 < j < 8) and a[i][j] == opponent:
                i, j = i + i2, j + j2
            if (-1 < i < 8) and (-1 < j < 8) and a[i][j] == player:
                return True
    return False

## 
def make_move(player):
    opponent = 1 if player == 2 else 2
    a[i1][j1] = player
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for i2, j2 in directions:
        i, j = i1 + i2, j1 + j2
        if (-1 < i < 8) and (-1 < j < 8) and a[i][j] == opponent:
            direct = [(i, j)]
            i, j = i + i2, j + j2
            while (-1 < i < 8) and (-1 < j < 8) and a[i][j] == opponent:
                direct.append((i, j))
                i, j = i + i2, j + j2
            if (-1 < i < 8) and (-1 < j < 8) and a[i][j] == player:
                for i3 , j3 in direct:
                    a[i3][j3] = player    

##  i j    
def ij(choice):
    i , j = choice//8 , choice%8 -1
    if(choice%8 == 0):
        i , j = choice//8 -1 , 7
    global i1                             
    i1 = i
    global j1
    j1 = j

#### MAIN ####

a = [[0 for _ in range(8)] for _ in range(8)]
a[3][3] = 1
a[3][4] = 2
a[4][3] = 2
a[4][4] = 1
display()                                      ## 
f = 0
nothing = 0
while(f < 64 and nothing < 2):
    if(f%2 == 0):                                ## 1 
        if(Is_there(2)):   
            choice=int(input(Fore.GREEN +"Player X"+" choose a location :"))
            if(65 > choice >0):
                ij(choice)
                if(is_valid_move(2)):              ##  
                    make_move(2)                   ##  
                    f += 1
                else:           
                    print(Fore.RED +"Invalid selection!!!")
            else:
                print(Fore.RED +"Illegal choice!!!")
            if(nothing == 1):
                nothing -= 1
        else:
            f -= 1
            nothing += 1
            continue
    else:                                      ##    2
        if(Is_there(1)): 
            choice=int(input(Fore.RED +("Player O")+" choose a location :"))
            if(65 > choice >0):
                ij(choice)
                if(is_valid_move(1)):              ##  
                    make_move(1)                    ##  
                    f += 1
                else:           
                    print(Fore.RED +"Invalid selection!!!")
            else:
                print(Fore.RED +"Illegal choice!!!")   
            if(nothing == 1):
                nothing -= 1
        else:
            f -= 1
            nothing += 1
            continue
    display()                                   ## 

caunt1 = 0
caunt2 = 0
for i in range(8):
    for j in range(8):
        if(a[i][j] == 1):
            caunt1 += 1
        elif(a[i][j] == 2):
            caunt2 += 1
if(caunt1 < caunt2):
    print(Fore.GREEN +"X -", caunt2 ,Fore.RED +"\nO -" ,caunt1 ,'\nWell done', Fore.GREEN +"X" ,'you won!!!  ')
elif(caunt1 > caunt2):
    print(Fore.GREEN +"X -", caunt2 ,Fore.RED +"\nO -" ,caunt1 ,'\nWell done', Fore.RED +"O",' you won!!!  ')
else:
    print( Fore.GREEN +"X -", caunt2 ,Fore.RED +"\nO -" ,caunt1 ,Fore.YELLOW +"\ndraw!!!")
        