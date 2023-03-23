x= int(input())
store=[]
for i in range(x):
    c=0
    num= input().split()
    for j in range(len(num)):
        if int(j+1)>len(num)-1:
            continue
        elif int(num[j+1])> 2*int(num[j]):
            c+=int(num[j+1])-2*int(num[j])
    store.append(c)
for i in store:
    print(i)

