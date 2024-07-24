def sum_of_digits(a):
    sum=0
    if(a==0):
        return 0
    digit=a%10
    sum=digit+sum_of_digits(a//10)
    return sum
num=int(input("enter any number:"))
result=sum_of_digits(num)
print(f'sum of diigts in {num} is {result}')