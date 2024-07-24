def isarmstrong(a):
    sum=0
    org=a
    while(a!=0):
        digit=a%10
        sum=sum+digit**3
        a//=10
    if(org==sum):
        return True
    else:
        return False
num=int(input("enter a number:"))
for i in range(0,num+1):
    if(isarmstrong(i)):
      print(i,end=' ')
