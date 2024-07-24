num=int(input("enter how many numbers to print in fibonacci series: "))
a,b=0,1
print(f'{a},{b}',end=',')
for i in range(0,num):
    c=a+b
    a=b
    b=c
    if(i==num-1):
        break
    print(c,end=',')
print(c,end='.')