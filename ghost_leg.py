n, m = input().split()
n= int(n)
m= int(m)
store=[]
for i in range(m):
    x = int(input())
    store.append(x)
c=0
val=[]
for i in range(n):
    ans = i
    for j in range(n):
        if store[(m-1)-(j)] == i+1:
            ans+=1
            x =store.index(store[(m-1)-j])
            for j in range(n):
                if store[x-j] == i+1:
                    ans+=1
                else:
                    val.append(ans)
                    break
print(val)



