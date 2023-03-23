n = int(input())
store = []
minus = []
for i in range(n):
    b, p = input().split()
    b = int(b)
    ans = (60 * b) / float(p)
    store.append(ans)
    minus.append(ans / b)
for i in range(len(store)):
    print(('{:.4f}'.format(store[i] - minus[i])) ,('{:.4f}'.format(store[i], 4)) , ('{:.4f}'.format(store[i] + minus[i])))
