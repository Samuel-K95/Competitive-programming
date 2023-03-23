x=bin(int(input()))
print(x)
store=[]
for i in range(len(x)):
    if x[len(x)-1-i] =="b":
        break
    else:
        store.append(x[len(x)-1-i])
c=1000
a=int(store[0])*pow(10, len(store)-1)
for i in range(len(store)):
    if i == 0:
        continue
    else:
        a+=int(store[i])*c
        c/=10
print(a)
