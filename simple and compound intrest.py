p=eval(input("enter the principal amount:"))
n=eval(input("enter the period of time in years:"))
r=eval(input("enter the rate of intrest:"))
si=(p*n*r)/100
ci=p*((1+r/100)**n)-p
print("simple intrest %f"%(si))
print("compound intrest %f"%(ci))
