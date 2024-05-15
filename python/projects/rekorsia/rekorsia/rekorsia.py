def memuza(a,n):
    if(n==0):
        return a[n]
    return (memuza(a[0:n],n-1)*(n) + a[n])/(n+1)

def sum1(a, n):
    if(n==1):
        return a[1]+a[0]
    return a[n]+ sum1(a[0:n], n-1)

def sum2(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum    

def afuch1(num):
    if(num<10):
        return num
    l="1" + (len(str(num))-1)*"0"
    return (num%10)*int(l) + afuch1(num//10)

def afuch2(num,a):
    if(num<10):
        return a+ num
    return afuch2(num//10 , (a+num%10)*10) 


print(afuch2(96355 , 0))



# a=[1,2,3,4,10]
# print(memuza(a,len(a)-1))
# print(sum1(a,len(a)-1))
# print(sum2(a))

def deter(a ,i ,j):
    if(len(a) == i+2):
        return a[i][j]*a[i+1][j+1] - a[i][j+1]*a[i+1][j]
    return 