x=int(input())
store=[]
a=[]
b=[]
c=[]
for i in range(x):
    y=input().split()
    store.append((y))
for i in range(len(store)):
    for j in range(len(store[i])):
        if int(store[i][j])<0:
            continue
        else:
            a.append(i+1)
            b.append(j+1)
            c.append(store[i][j])
print(len(c))
for i in range(len(a)):
    print(a[i], b[i], c[i])



