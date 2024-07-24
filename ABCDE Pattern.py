for i in range(1,6):
    for j in range(0,i):
        print(chr(65+j),end='\t')
    print(end='\n')

for i in range(1,6):
    for j in range(0,i):
        print((chr(65+j)*i),end='\t')
    print(end='\n')