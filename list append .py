marks=[]
n=int(input("Enter the no. of subjects:"))
for i in range(0,n):
    a=int(input(f"enter the mark {i+1}:"))
    marks.append(a)
print(f"highest marks={max(marks)}")
print(f"lowest marks={min(marks)}")
marks.reverse()
print(marks)