n=int(input())
c=1
height =0
for i in range(n):
    if n-(pow(c, 2)) < 0:
        break
    else:
        height+=1
    n-=(pow(c, 2))
    c+=2
print(height)

