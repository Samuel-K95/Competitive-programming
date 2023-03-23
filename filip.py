x, y =input().split()
x =int(x)
y = int(y)
revx = 0
revy=0
while x>0:
    rem= x%10
    revx = revx*10 + rem
    x= x//10
while y>0:
    remy= y%10
    revy = revy*10 + remy
    y= y//10
if revx>revy:
    print(revx)
else:
    print(revy)
