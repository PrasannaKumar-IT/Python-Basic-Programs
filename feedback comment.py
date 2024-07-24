comment={5:'Excellent',4:'Very Good',3:'Good',2:'Satisfactory',1:'poor'}
rating=int(input('Enter your ratting (1-5):'))
if rating in comment:
    print('feedback comment:',comment[rating])
else:
    print("invalid input")