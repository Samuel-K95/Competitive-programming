n = int(input())
store = []
for i in range(n):
    store.append(int(input()))
c = 1
for i in range(len(store)):
    print(store[-c])
    c += 1
