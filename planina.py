n = int( input())
a = 2
c = 1
for i in range(n):
    N = a + pow(2, c-1)
    a = N
    c+=1
print(pow(N, 2))