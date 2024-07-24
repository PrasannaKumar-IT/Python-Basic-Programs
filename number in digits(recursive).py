def number_of_digits(a):
    sum=0
    if(a==0):
        return 0
    sum=1+number_of_digits(a//10)
    return sum
num=int(input("enter any number:"))
result=number_of_digits(num)
print(f'sum of diigts in {num} is {result}')