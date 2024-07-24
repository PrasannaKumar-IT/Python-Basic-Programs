def reverse(a):
    rev=0
    while(a!=0):
        digit=a%10
        rev=rev*10+digit
        a=a//10
    return rev
num=int(input("Enter the number:"))
rev=reverse(num)
print(rev)