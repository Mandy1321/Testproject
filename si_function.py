def Simpleinterest(P,T,R):

    si=P*T*R/100
    return si
principle=int(input("enter the principle amount:"))
time=int(input("enter the time amount:"))
rate=int(input("enter the rate amount:"))
interest=Simpleinterest(principle,time,rate)
print(interest)
