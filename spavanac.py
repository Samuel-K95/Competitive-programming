a, b = input().split()
a = int(a)
b = int(b)
if b < 45:
    if a == 0:
        a = 23
    else:
        a-=1
    x = 45 - b
    b = 60 - x
else:
    b = b - 45
print (a, b)