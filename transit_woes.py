s, t, n = input().split()
N = input().split()
b = input().split()
c = input().split()
s= int(s)
t= int(t)
n= int(n)
store=[]
for i in N:
    i= int(i)
for i in b:
    i= int(i)
for i in c:
    i = int(i)
for i in range(len(N)):
    if i == len(N)-1:
        store.append(N[i])
    elif c[i]==0:
        continue
    else:
        store.append(int(N[i]))
        store.append(int(c[i]))
sum=0
for i in store:
    i=int(i)
    sum+=i

if sum > (t-s):
    print("No")
else:
    print("yes")


