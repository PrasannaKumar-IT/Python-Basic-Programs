import sys
square_list=[i*i for i in range(0,6) ]
print(square_list)
list_iterator=iter(square_list)
try:
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
    print(next(list_iterator))
except:
    print(sys.exc_info()[0])
finally:
    print("The end")
