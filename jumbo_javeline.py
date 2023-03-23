n = int(input())
store = []
for i in range(n):
    x = int(input())
    store.append(x)
sum = 0
for i in store:
    sum += i
print(sum-(len(store)-1))
