# כתוב קטע בפעולה ראשית )main )שיקלוט מספרים שלמים. הקלט יסתיים כאשר ייקלט מספר .0
# על התוכנית לחשב ולהדפיס:
# - כמה מספרים נקלטו.
# - כמה מספרים זוגיים נקלטו.
# - ממוצע מספרים חיוביים שנקלטו.
# הערה: אפשר להניח שיש לפחות מספר אחד חיובי.
# a=0
# c=0
# d=0
# e=0
# sum=0
# while(a==0):
#     b=int(input("pleas enter a number :"))
#     c+=1
#     if(b==0):
#         a+=1
#     if(b%2==0):
#         d+=1
#     if(b>0):
#         e+=1
#         sum+=b
# print(c)   
# print(d)  
# print(sum/e)  




#  כתוב פעולה שמקבלת מערך מספרים שלמים ומחזירה ערך true אם הוא "מערך מאוזן", ולא הפעולה
# תחזיר ערך false

def meuzan(a):
    if(len(a)%2==0 or len(a)<3):
        return False
    s=(len(a)//2)
    for u in range(s):
        if(a[u]<a[s] or a[len(a)-1-u]>a[s]):
            return False
    return True    
        

### MAIN  ###


i=int(input("pleas enter the Length : "))
a=[0]*i
for i in range(len(a)):
    a[i]=int(input("pleas enter a number : "))
print(meuzan(a))
