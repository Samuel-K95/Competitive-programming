x= int(input())
store=[]
for i in range(x):
    a,b=input().split()
    a=int(a)
    b=int(b)
    sum=0
    for i in range(b+1):
        sum+=i
    sum+=b
    store.append(sum)
for i in range(len(store)):
    print((i+1), store[i])