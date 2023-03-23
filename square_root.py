import math
n = int(input())
val = []
ans= 0
for i in range(n):
    x = int(input())
    for j in range(x):
        if (x-j) % math.sqrt(x-j) == 0 :
            ans = int(math.sqrt(x-j))
            val.append(ans)
            break
for i in val:
    print(i)
