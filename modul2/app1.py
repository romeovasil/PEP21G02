x=input("Get time1")
y=input("Get time2")

hour1=int(x[:2])
min1=int(x[3:5])
sec1=int(x[6:8])


hour2=int(y[:2])
min2=int(y[3:5])
sec2=int(y[6:8])

t1=3600*hour1+60*min1+sec1

t2=3600*hour2+60*min2+sec2


print(t2-t1)