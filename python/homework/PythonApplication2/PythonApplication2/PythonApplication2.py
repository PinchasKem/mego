for j in range(1,11):
    for i in range(1,11):
        print(i*j ,end=", ")
    print()
    
def if_brothers(a,b):
    if(a%10!=b%10):
        return False 
    while(a>9):
        a=a//10
    while(b>9):
        b=b//10
    return a==b    
           
     



def if_braders(a,b): 
    a=str(a)
    b=str(b)            
    if(a[0]==b[0] end a[-1]==b[-1]):
        return True
    return False   