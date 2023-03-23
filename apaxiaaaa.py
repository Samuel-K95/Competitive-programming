x = input()
store = []
for i in range(len(x)):
    if i ==0:
        store.append(x[i])
    elif x[i-1]==x[i]:
       continue
    else:
        store.append(x[i])
for i in store:
    print(i, end="")
