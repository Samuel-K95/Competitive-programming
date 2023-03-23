l1 = input().split()
l2 = input().split()
store = []
for i in range(len(l1)):
    store.append(int(l1[i]) + int(l2[i]))
for i in range(len(store)):
    print(store[(len(store) - 1) - i], end=" ")