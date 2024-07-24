list=[34,56,78,90,32,14,56,66]
largest=list[0]
second_largest=list[0]
for i in list:
    if i>largest:
        largest=i
for i in list:
    if i>second_largest and i<largest:
        second_largest=i
print(second_largest)