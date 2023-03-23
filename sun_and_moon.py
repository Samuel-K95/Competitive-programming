x, y= input().split()
a, b = input().split()
lcm =(int(y)-int(x))*(int(b)-int(a))
for i in range(lcm):
    if i/(int(y)-int(x))==(int(b)-int(a)) and i/(int(b)-int(a))==(int(y)-int(x)):
        lcm = i
print(lcm)