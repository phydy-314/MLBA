import random
list=[]
for i in range (10):
    x=random.Random().randint(0,100)
    list.append(x)
print(list)
print("Gia tri tai phan tu thu 2 =", list[2])

def isprime(x):
    count=0
    for i in range (1,x+1):
        if x%i==0:
            count=count+1
    return count==2
def listprime(list):
    for item in list:
        if isprime(item):
            print(item, end=' ')
print("Cac so nguyen to trong danh sach:")
#CRUD, Create, Retrieved, Update, Delete
listprime(list)