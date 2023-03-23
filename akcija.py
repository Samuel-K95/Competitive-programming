n = int(input())
store = []
for i in range(n):
    x = int(input())
    store.append(x)
for i in store:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
