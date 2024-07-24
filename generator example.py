def cube_generator(n):
    value=0
    while value<n:
        yield value**3
        value+=1
for i in cube_generator(10):
    print(i)
