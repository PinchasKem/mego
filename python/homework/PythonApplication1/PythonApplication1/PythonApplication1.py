
# def reduce_matrix(a):
#     new_matrix=[ [0] * (len(a)-1) ] * (len(a[0])-1)
#     for j in range(len(a[0])-1):
       

# def mul_deter(a):
#     mul= a[0][0]*a[1][1] - a[0][1]*a[1][0]
#     return mul


# a=[
#     [23,56,65,95],
#     [56,25,85,74],
#     [89,5,65,235],
# ]

# if(len(a) > 3):
#     reduce_matrix(a)
# else:
   
   


# def psagot(a):
#     i=1
#     while(i<len(a)-1):
#        if(a[i]>a[i-1]):
#            if(a[i]>a[i+1]):
#                 print(a[i])
#                 i+=2
#            else:
#                i+=1
#        else:
#            i+=1    



# a=[6,5,1,0,6,8,2,3,5,6,9,8,5,2,3,6,5,8,9,6]
# print(psagot(a))


# def k(a):
#     i=0
#     while(i<len(a)-1):
#         if(a[i]<a[i+1]):
#             i+=1
#         else:
#             q=i
#             while(i>0 and i<len(a)-1):
#                 if(a[i]>a[i+1]):
#                     i+=1
#                 else:
#                     return -1
#     return q            


# a=[6,5,1,0]
# print(k(a))



# import random        
 
# a=[0]*1000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# print(a)
# caunters=[0]*101
# for l in range(len(a)):
#     caunters[a[l]]+=1
# print(caunters)    
# index=0
# for i in range(101):
#     k=0
#     while(k<caunters[i]):
#         a[index]=i
#         index+=1
#         k+=1
# print(a)        
       
   




# def aj(a,v):
#      for i in range(len(a)-1):
#          for j in range(len(a[i])-1):
#              if(a[i][j]=v):
#                  if(a[i][j+1]=v):
#                      if(a[i+1][j]=v):
#                          if(a[i+1][j+1]):
#                              return True
#      return False            


# a=[[1,2,6],
#    [6,9,7],
#    [5,0,3],
# ]

# b=[[1,2,6],
#    [6,9,7],
#    [5,0,3],
# ]
# print(aj(a,7))



# for i in range(len(a)):
#     for j in range(len(a)):
#         b[len(a)-1-j][i]=a[i][j]
# print(b)


# a=[[12,32,65,23],[12,36,58,52],[65,21,45,95]]
# b=[[12,52],]
# for e in range(len(a))

# left=[
#     [2,5,4,6],    
#     [9,3,1,4],    
# ]
# right=[
#     [4,7,9],    
#     [1,2,3],    
#     [9,6,7],    
#     [3,2,3],    
# ]
# m=[
#     [0,0,0],
#     [0,0,0],
#   ]
# for r in range(len(left)):
#     for c in range(len(right[0])):
#         sum=0
#         for i in range(len(left[0])):
#             sum+=left[r][c]*right[c][i]  
#         m[r][c]=sum
# print(m)





# b=int(input("Type the number of exercises : "))
# a=[]
# for i in range(b):  
#     num = input("Enter numbers:" )
#     d = [float(sam) for sam in num.split(',')]  
#     a.append(d)



# def fun(i,j,a):
#     for x in range(len(a)):
#         if(x!=i):    
#             for z in range(len (a)):
#                 if(z!=j):
#                     a[x][z]=a[i][j]
#                     j+=1
#             i+=1
#     print(a)            
   

# a=[[12,32,65,23],[12,36,58,52],[65,21,45,95]]
# print(fun(0,0,a))



# deter=0
# for u in range(len(a)):
#     if(u==len(a)-2):
#         num=0
#         for c in range(num+1):
#             deter+=(a[u][u]*a[u+1][u+1])-(a[u][u+1]*a[u+1][u])
# for i in range(len(a)):
#     if(i)



# with open(r"C:\Users\USER\Documents\veb.txt","r") as file1:
#     r=file1.read()
# with open(r"C:\Users\USER\Documents\veb2.txt","a") as file2:
#     file2.write(r)



# text=input_file.read()
# print(text)
# text=input_file.readline()
# print(type(input_file))
# print(text)


# פתרון מטריצות

b=int(input("Type the number of exercises : "))
a=[]
for i in   range(b):  
    num = input("Enter numbers:" )
    d = [float(sam) for sam in num.split(',')]  
    a.append(d)
for i in range(len(a)):
    c=float(a[i][i])
    for y in range(len(a)):
        if(y!=i):
            q=float(a[y][i])
            p=0
            for p in range(len(a)+1):
                v=float(c*a[y][p])
                m=float(a[i][p]*-q)
                a[y][p]=m+v
for i in range(len(a)):
    print(i+1 , ".  " ,a[i][len(a)]/a[i][i])
   
# # חישוב דטרמיננטה ופתרון לפי קרמר

# # b=int(input("Type the number of exercises : "))
# # a=[]
# # for i in   range(b):  
# #     num = input("Enter numbers:" )
# #     d = [float(sam) for sam in num.split(',')]  
# #     a.append(d)
# # a=[[1,2,5],[2,3,5]]
# # for i in range(len(a)):
# #     c=float(a[i][i])
# #     for y in range(len(a)):
# #         if(y!=i):
# #             q=float(a[y][i])
# #             p=0
# #             for p in range(len(a)+1):
# #                 v=float(c*a[y][p])
# #                 m=float(a[i][p]*-q)
# #                 a[y][p]=m+v
# # for i in range(len(a)):
# #     print(i+1 , ".  " ,a[i][len(a)]/a[i][i])
   




# import random
# c=0
# p=0
# for i in range(100):
#     num=random.randint(1000,9999)
#     if(num%2==0):
#         print(num,num//1000)
#     else:
#         print(num,num%10)
#     if(num%10==4):
#         p+=1
#     for s in range(4):
#         if(num%10==6):
#             c+=1
#         num=num//10
# print(c)
# print(p)

# c=0
# for i in range(39):
#     num=random.randint(100,999)
#     c+=num
#     if(num%2==0):
#         print(num%10 + (num//10)%10 + num//100)
# print(c /39)



# i=40
# b=0
# c=0
# while(i>0):
#     num=int(input("Enter a number :"))
#     if(num>99 and num<1000):
#         print(num%10 + (num//10)%10 + num//100)
#     if(num%2==0):
#         b+=1
#     else:
#         c+=num
#     i-=1
# print(b)
# print(c)

# חישוב של סך מספרים רגילים זוגיים וממוצע

# num=int(input("Enter a number :"))
# c=0
# z=0
# p=0
# s=0
# while(num!=0):
#    c+=1
#    if(num%2==0):
#       z+=z
#    if(num>0):
#       p+=1
#       s+=num
#    num=int(input("Enter a number :"))
# print(c)
# print(z)
# print(s/p)


# שיתוף בין פונקציית כפל לחזקה

# def mul(a,b):
#     r=0
#     while(a>0):
#         r+=b
#         a-=1
#     return r


# def hezka(x,y):
#     t=1
#     while(y>0):
#         # t=mul(x,t)
#         t=x*t
#         y-=1
#     return t



# פונקציה לחיבור של ספרות בסדר עולה


# def F(x):
#     r=0
#     i=1
#     while(i<x):
#         r+=i
#         i+=1
#     return r



# for i in range(3,8):
#     print(F(i))

# פונקציה למציאת מספר ראשוני

# import math
# def IsPrime(x):
#     if(x%2==0):
#         print("no")
#     else:
#         sqrtx=int(math.sqrt(x))+1
#         for i in range(3,sqrtx,2):
#             if(x%i==0):
#                 print("no")
#                 break
#             if(i>=sqrtx-2):
#                 print("yes")
           

   


# ###    MAIN    ####

# num=int(input("Enter a number:"))        
# IsPrime(num)


# פונקציה למציאת מחלקים

# import math
# def showDeviders(x):
#     sqrtx=int(math.sqrt(x))
#     for i in range(2,sqrtx,1):
#         if(x%i==0):
#             print(i,"  ", x//i)
#     i+=1
#     if(x%i==0):
#         if(x//i!=i):
#             print(i,x//i)
#         else:
#             print(i)    


   
       


# ###    MAIN    ####

# num=int(input("Enter a number:"))        
# showDeviders(num)

