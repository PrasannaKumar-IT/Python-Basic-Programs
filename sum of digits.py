def sum_of_digits(a):
    b=str(a)
    sum=0
    for i in b:
        sum=sum+int(i)
    return sum
num=int(input("enter any number:"))
result=sum_of_digits(num)
print(f'sum of diigts in {num} is {result}')