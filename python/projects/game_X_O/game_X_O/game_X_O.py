# from ast import Global

# from colorama import Fore, Back, Style, init
# init()

# ### פונקציית הצגה
# def display():
#     print('    ','-'*11)
#     r=1
#     q=[ 1,Fore.RED + '| O ' ,Fore.BLUE + '| X ']
#     for i in range(3):
#         print('    ', end = '')
#         for j in range(3): 
#             q[0] = F'| {i*3+j+1} ' 
#             print(q[a[i][j]], end = '')
#             r+=1    
#         print('|')
#     print('    ','-'*11)

# ##  בדיקת מקום פנוי
# def legal_choice(i,j):
#     if(a[i][j]>0):
#         return False
#     return True

# ##  השמת ערך בטבלה
# def player(choice,z):
#     if(choice%3==0):
#         i=choice//3-1
#         j=2
#     else:    
#         i=choice//3
#         j=choice%3-1
#     a[i][j]=z
#     global i1                                ## משתנים לצורך בדיקת הנצחון
#     i1 = i
#     global j1
#     j1 = j
#     return i,j

# ## בדיקת נצחון
# def if_win(i1,j1):
#     if(a[i1][0] == a[i1][1] == a[i1][2]):    
#         return True
#     if(a[0][j1]==a[1][j1] == a[2][j1]):
#         return True
#     if(a[0][2]==a[1][1] == a[2][0] and a[0][2]>0):
#         return True
#     if(a[2][2] == a[1][1] == a[0][0] and a[2][2]>0):
#         return True
#     return False

# ##  הצגת נצחון
# def win(i):                             
#     if(i%2==1):
#         print("Congratulations to player 1, you won!!")
#     else:
#         print("Congratulations to player 2, you won!!")


# #### MAIN ####

# a = [[0 for _ in range(3)] for _ in range(3)]  ## יצירת הטבלה הראשית
# i1=0                                           ## משתנים לצורך בדיקת הנצחון
# j1=0
# display()                                      ## קריאה לפונקצית הצגה

# i=0
# while(i<9):
#     if(i%2==0):                                ## 1 בחירת שחקן
#         choice=int(input("Player 1 choose a location :"))
#         if(a[i][j]>0):               ##  בדיקת מקום פנוי
#             i,j = player(choice,2)   ##  שליחה להשמת ערך בטבלה          
#             i+=1
#         else:           
#             print("Invalid selection!!!")
#     else:                                      ##  בחירת שחקן 2
#         choice=int(input("Player 2 choose a location :"))
#         if(a[i][j]>0):               ##  בדיקת מקום פנוי
#             i,j = player(choice,1)   ##  שליחה להשמת ערך בטבלה          
#             i+=1
#         else:
#             print("Invalid selection!!!")    
#     display()                                   ## קריאה לפונקצית הצגה
#     if(i>4):                                    ##  שליחה לבדיקת נצחון
#         if(if_win(i1,j1)):
#             win(i)
#             break
#     if(i==9):
#         print("Ended in a draw, try again!!")

from ast import Global
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)



### הצגת טבלה
def display():
    print('    ','-'*11)
    r=1
    for i in range(3):
        print('    ', end = '')
        for j in range(3):            
            q=[ r  ,Fore.RED + 'O' ,Fore.BLUE + 'X']
            print(F'| {q[a[i][j]]} ', end = '')
            r+=1    
        print('|')
    print('    ','-'*11)

##  בדיקת מקום פנוי
def legal_choice(choice):
    if(choice%3==0):
        i=choice//3-1
        j=2
    else:    
        i=choice//3
        j=choice%3-1
    if(a[i][j]>0):
        return False
    return True

##  השמת ערך בטבלה
def player(choice,z):
    if(choice%3==0):
        i=choice//3-1
        j=2
    else:    
        i=choice//3
        j=choice%3-1
    a[i][j]=z
    global i1                                ## משתנים לצורך בדיקת הנצחון
    i1 = i
    global j1
    j1 = j

## בדיקת נצחון
def if_win(i1,j1):
    if(a[i1][0] == a[i1][1] == a[i1][2]):    
        return True
    if(a[0][j1]==a[1][j1] == a[2][j1]):
        return True
    if(a[0][2]==a[1][1] == a[2][0] and a[0][2]>0):
        return True
    if(a[2][2] == a[1][1] == a[0][0] and a[2][2]>0):
        return True
    return False

##  הצגת נצחון
def win(i):                             
    if(i%2==1):
        print("Congratulations to player 1, you won!!")
    else:
        print("Congratulations to player 2, you won!!")


#### MAIN ####

a = [[0 for _ in range(3)] for _ in range(3)]  ## יצירת טבלה
i1=0                                           ## משתנים לצורך בדיקת הנצחון
j1=0
display()                                      ## שליחה להצגה

i=0
while(i<9):
    if(i%2==0):                                ## 1 בחירת שחקן
        choice=int(input("Player 1 choose a location :"))
        if(legal_choice(choice)):              ##  בדיקת מקום פנוי
            player(choice,2)                   ##  השמת ערך בטבלה
            i+=1
        else:           
            print("Invalid selection!!!")
    else:                                      ##  בחירת שחקן 2
        choice=int(input("Player 2 choose a location :"))
        if(legal_choice(choice)):              ##  בדיקת מקום פנוי
            player(choice,1)                   ##  השמת ערך בטבלה
            i+=1
        else:
            print("Invalid selection!!!")    
    display()                                   ## שליחה להצגה
    if(i>4):                                    ## שליחה לבדיקת נצחון
        if(if_win(i1,j1)):
            win(i)
            break
    if(i==9):
        print("Ended in a draw, try again!!")