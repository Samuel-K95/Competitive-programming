x = input()
store=[]
for i in range(len(x)):
    for j in range(len(x)):
        if i == j:
            continue
        elif x[i] == x[j]:
            store.append(1)
        else:
            store.append(0)
if 1 in store:
    print(0)
else:
    print(1)