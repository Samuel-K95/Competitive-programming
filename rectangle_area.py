x, y= input().split()
a, b = input().split()
lcm =(int(y)-int(x))*(int(b)-int(a))
for i in range(lcm):
    if i == 0:
        continue
    elif i/(int(y)-int(x))==0 and i/(int(b)-int(a))==0:
        lcm = i
print(lcm)