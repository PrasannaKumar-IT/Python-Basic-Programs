weekdays={1:'sunday',2:'monday',3:'tuesday',4:'wednesday',5:'thursday',6:'friday',7:'saturday'}
days=int(input("enter a day(1-7):"))
if days in weekdays:
    print(f'{days}-{weekdays[days]}')
else:
    print("invalid input")6