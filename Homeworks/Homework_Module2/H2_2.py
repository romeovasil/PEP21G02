# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print the difference between them in the
# received format dd:hh:mm:ss
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)

time1=input("Insert time1 in format dd:hh:mm:ss")
time2=input("Insert time2 in format dd:hh:mm:ss")

D1=int(time1[:2])
D2=int(time2[:2])

H1=int(time1[3:5])
H2=int(time2[3:5])

M1=int(time1[6:8])
M2=int(time2[6:8])

S1=int(time1[9:])
S2=int(time2[9:])

totalTime1=D1*24*60*60+H1*60*60+M1*60+S1
totalTime2=D2*24*60*60+H2*60*60+M2*60+S2

if totalTime1>totalTime2:
    diffTime=totalTime1-totalTime2
else:
    diffTime=totalTime2-totalTime1

D3=diffTime//(24*60*60)
diffTime=diffTime%(24*60*60)
H3=diffTime//(60*60)
diffTime=diffTime%(60*60)
M3=diffTime//(60)
S3=diffTime%(60)

print(D3,H3,M3,S3,sep=":")