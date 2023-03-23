x= input().split()
w=[3,2,1]
store=[]
store1=[]
V=["Province", "Duchy", "Estate"]
Vcost=[8,5,2]
T=["Gold", "Silver","Copper"]
Tcost=[6, 3, 0]
y=0
for i in range(len(x)):
    x[i]=int(x[i])*w[i]
    y+=int(x[i])
for i in range(len(Vcost)):
    if y >= Vcost[i]:
        store.append(V[i])
        break
    else:
        continue
for i in range(len(Tcost)):
    if y >= Tcost[i]:
        store.append(T[i])
        break
    else:
        continue
if len(store)>1:
    print(store[0], "or", store[1])
else:
    print(store[0])



