n = int(input())
ans=[]
for i in range(n):
    a, b= input().split()
    a = int(a)
    b = int(b)
    ans.append(a%b)
for i in ans:
    print(i)
