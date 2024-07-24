def is_prime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
num=int(input("enter a number:"))
for i in range(0,num+1):
    if(is_prime(i)):
     print(i,end=' ')
