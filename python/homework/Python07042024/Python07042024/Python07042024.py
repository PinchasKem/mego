
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
# # else:
    

# def deter2(a):
#     mone=0
#     new=[[0]*(len(a)-1) for t in range(len(a)-1)]
#     for u in range(len(a)):    
#         m=0
#         for i in range(1,len(a)):
#             l=0
#             for j in range(len(a)):
#                 if(j!=u):
#                     new[m][l]=a[i][j]
#                     l+=1
#             m+=1
#         if(u%2==0):
#             s=a[0][u]
#         else:
#             s=-a[0][u]
#         mone+=s*deter1(new[0][0],new[0][1],new[1][0],new[1][1])                    
#     return mone        




# def deter3(a):
#     if(len(a)==3):
#         return print(deter2(a))
#     elif(len(a)==2):
#         return print(deter1(a))
#     mone=0
#     new=[[0]*(len(a)-1) for t in range(len(a)-1)]
#     for u in range(len(a)):    
#         m=0
#         for i in range(1,len(a)):
#             l=0
#             for j in range(len(a)):
#                 if(j!=u):
#                     new[m][l]=a[i][j]
#                     l+=1
#             m+=1
#         if(u%2==0):
#             s=a[0][u]
#         else:
#             s=-a[0][u]
#         if(len(new)>2):            
#             mone+=s*deter2(new)
#         else:
#             mone+=s*deter1(new[0][0],new[0][1],new[1][0],new[1][1])        

###########################################################################################

# def deter2(a,b,c,d):
#     return (a*d-b*c)



# def deter3(a):
#     new=[[0]*(len(a)-1) for t in range(len(a)-1)]
#     mone=0
#     for u in range(len(a)):    
#         m=0
#         for i in range(1,len(a)):
#             l=0
#             for j in range(len(a)):
#                 if(j!=u):
#                     new[m][l]=a[i][j]
#                     new[m][l]*=-1 
#                     l+=1
#             m+=1
#         if(u%2==0):
#             s=a[0][u]
#         else:
#             s=-a[0][u]
#         new[0][0]*=s
#         new[1][0]*=s
#         mone+=deter4(new)
#     return mone    

# def deter1(a):
#     if(len(a)==2):
#         return deter2(a[0][0],a[0][1],a[1][0],a[1][1])
#     else:
#         return deter3(a,0)

# def deter4(a):
#     if(len(a)==2):
#         return deter2(a[0][0],a[0][1],a[1][0],a[1][1])
#     else:
#         return deter3(a)    
###########################################################################################

# a=[[1,2,2],
#    [5,6,5],
#    [5,9,7],     
#     ]
# print(deter1(a))

# b=[[10,2,2],
#    [11,6,5],
#    [15,9,7],    
#      

# print(deter1(b))


# a=[[1,2,2,3],
#    [5,6,5,5],
#    [5,9,7,8],    
#    [5,4,7,12],    
#     ] 
# print(deter1(a))

# b=[[10,2,2,3],
#    [11,6,5,5],
#    [15,9,7,8],    
#    [20,4,7,12],    
#     ]

# print(deter1(b))


 
 
a=[[5,6,9,8,6,5],
   [5,9,9,4,6,5], 
   [5,6,9,21,6,5],
   [5,6,9,8,65,5],
   [5,56,9,8,6,32],
   [5,6,9,86,98,5],
   ]
d= len(a) 
h= 1
for i in range(len(a)-2):
    h*= d
    d-= 1
for u in range(h):
    for i in range(len(a)-3):
        
        





# import random
# def BinariSearch(a, x):
#     low=0
#     up=len(a)-1
#     while(low<=up):
#         mid=(low+up)//2
#         if(x==a[mid]):
#             return mid
#         if(x<a[mid]):
#             up=mid-1
#         else:
#             low=mid+1
#     return -1
# def Search(a, x):
#     for i in range(len(a)):
#         if(a[i]==x):
#             return i
#     return -1
   
# a=[0]*10000000
# a[0]=2
# for i in range(1,len(a)):
#     a[i]=a[i-1]+random.randint(1,6)
# print(a)    
# y=int(input("Enter a number : "))
# print(Search(a, y)) 






# def miun(a):
#     for i in range(len(a)-1):
#         if(a[i]%2==1):
#             for u in range(i+1,len(a)):
#                 if(u==len(a)):
#                     return a
#                 if(a[u]%2==0):
#                     ezer=a[u]
#                     a[u]=a[i]
#                     a[i]=ezer
#                     break


# s=[23,5,68,85,65,35,88,658,234,56]
# miun(s)
# print(s)




# def miun(a):    
#     right=len(a)-1
#     left=0
#     while(left<len(a) and a[left]%2==0):
#         left+=1
#     if(left<len(a)-1):
#         while(left<right and a[right]%2==1):
#             right-=1
#         while(left<right):
#             if(a[right]%2==0 and a[left]%2==1):
#                 ezer=a[left]
#                 a[left]=a[right]
#                 a[right]=ezer
#                 right-=1
#                 left+=1
#             else:
#                 if(a[right]%2==1):
#                     right-=1
#                 if(a[left]%2==0):
#                     left+=1
    



# s=[23,5,68,85,65,35,88,658,234,56]
# miun(s)
# print(s)

# a=[
#     [2,3,6,5,8,8],
#     [5,8,9,5,4,5],
#     [2,3,6,2,8,5],
#     [5,5,6,5,9,9],
#     [6,1,6,2,8,5],
#     [9,6,6,5,8,2],
#     ]
# c=0
# for i in range(len(a)-1):
#     for u in range(len(a[i])-1):
#         if(a[i][u]==a[i][u+1]):
#             c+=1
#         if(a[i][u]==a[i+1][u]):
#             c+=1
#     for i in range(len(a)-1):
#         if(a[i][len(a)[i]]==a[i+1][len(a)[i]]):
#             c+=1
#     for i in range(len(a)[0]-1):
#         if(a[len(a)[i]][i]==a[len(a)[i]][i+1]): 
# print(c)
    



# a=[
#     [2,3,6,5,8,8],
#     [5,8,9,5,4,5],
#     [2,3,6,2,8,5],
#     [5,5,6,5,9,9],
#     [6,1,6,2,8,5],
#     [9,6,6,5,8,2],
#     ]
# for i in range(len(a[0])):
#     max=a[0][i]
#     for u in range(1, len(a)):
#        if(max<a[u][i]):
#            max=a[u][i]
#     print(max)





# import random
# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
           
# r=ord('a')
# s=""
# for i in range(3000000):
#     c=chr(random.randint(97,106))
#     s=s+c
# # print(s)
# m= [[0 for x in range(10)] for y in range(10)]
# for i in range(len(s)-1):
#     sh=ord(s[i])-97
#     a=ord(s[i+1])-97
#     m[sh][a]+=1
# rMax=0
# cMax=0
# for r in range(len(m)):
#     for c in range(len(m)):
#         if(m[rMax][cMax]<m[r][c]):
#             rMax=r
#             cMax=c
# print(rMax, cMax)
# print(chr(rMax+97), chr(cMax+97))
# Show(m)    

# w, h = 8, 5
#   fcea
#   abcdef


# # def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)
   
# names=["khimon", "oosef", "gad", "yosef", "dan", "gadi"]          
# print(names)
# for niv in range(len(names)-1):
#     for bod in range(niv+1, len(names)):
#         if(CmpString(names[niv], names[bod])<0):
#             temp=names[bod]
#             names[bod]=names[niv]
#             names[niv]=temp
# print(names)          
#   reuven      levi        >0
#   levi        reuven      <0
#   levi        levi        ==0
#   levi        levin        <0
#   levin       levi        >0
#   levarov     levi        ==0
#   ran         binyamin


#   levin '/0'       levi '/0'
