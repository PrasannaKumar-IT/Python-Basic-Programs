a,b,c=[int(x) for x in input("enter three numbers (splitted by \',\'): ").split(',')]
if(a>=b and a>=c):
    if(b>c):
        print(f'{b} is second largest among three')
    else:
        print(f'{c} is second largest among three')
elif(b>=c and b>=a):
    if(c>a):
        print(f'{c} is second largest among three')
    else:
        print(f'{a} is second largest among three')
else:
    if(a>c):
        print(f'{a} is second largest among three')
    else:
        print(f'{b} is second largest among three')