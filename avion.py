store=[]
c=1
for i in range(5):
    x= input()
    for i in x:
        if "FBI" in x:
            store.append(c)
            break
    c+=1
if len(store) == 0:
    print("HE GOT AWAY!")
else:
    for i in store:
        print(i, end=" ")