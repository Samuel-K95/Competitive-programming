n = int(input())
store = []
check = []
ans =[]
for i in range(n):
    x = int(input())
    for i in range(x):
        y = input()
        store.append(y)
    val = 0
    for j in store:
        if j in check:
            continue
        else:
            check.append(j)
            val += 1
    ans.append(val)
for i in ans:
    print(i)
