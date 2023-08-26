N, S = input().split()
N = int(N)
dom = {'A': 11, 'K': 4, 'Q' : 3, 'J' : 20, 'T' : 10, '9' : 14, '8' : 0, '7' : 0}
Nondom = {'A': 11, 'K': 4, 'Q' : 3, 'J' : 2, 'T' : 10, '9' : 0, '8' : 0, '7' : 0}
sum = 0
for i in range(4*N):
    comm = input()
    if comm[1] == S:
        sum += dom[comm[0]]
    else:
        sum += Nondom[comm[0]]
print(sum)