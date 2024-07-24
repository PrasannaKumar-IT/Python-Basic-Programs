def isarmstrong(a):
    sum=0
    while(a!=0):
        digit=a%10
        sum=sum+digit**3
        a//=10
    return sum
num=int(input("enter a number:"))
sum=isarmstrong(num)
if(num==sum):
    print(f'{num} is a Armstrong Number')
else:
    print(f'{num} is not a Armstrong Number')