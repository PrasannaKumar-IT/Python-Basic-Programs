def count_odd_even(a):
    b=str(a)
    odd=0
    even=0
    for i in b:
        if(int(i)%2==0):
            odd+=1
        else:
            even+=1
    return odd,even
num=int(input("Enter Number:"))
odd,even=count_odd_even(num)
print(f'number of odd numbers {odd}')
print(f'number of even numbers {even}')