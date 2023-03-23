n = int( input())
store=[]
x = 0
for i in range(n):
    store.append(int(input()))
if n % 2 != 0:
    print("still running")
else :
    c=0
    for i in range(len(store)):
        if (c+1)> len(store):
            break
        x+=(store[c+1]-store[c])
        c+=2
    print(x)