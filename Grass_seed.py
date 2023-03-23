n= float(input())
x = int(input())
val = 0
for i in range(x):
    a, b = input().split()
    a= float(a)
    b= float(b)
    val += (a*b)*n
print('{:.7f}'.format(val))