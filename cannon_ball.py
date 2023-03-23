import math
x=int(input())
store=[]
for i in range(x):
    val = input().split()
    t=float(val[2])/(float(val[0])*math.cos(3.14/4))
    if ((float(val[0])*math.sin((math.pi*float(val[1]))/180))*t)-(9.8/2)*math.pow(t,2) > (float(val[3])+1) and (float(val[0])*math.sin((math.pi*float(val[1]))/180))*t-(9.8/2)*math.pow(t,2) < (float(val[4])-1):
        store.append("Safe")
    else:
        store.append("Not Safe")
for i in store:
    print(i)
