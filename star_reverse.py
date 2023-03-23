n = []
m = []
correct= []
while True:
    x, y, z = input().split()
    if int(x) == -1:
        y = None
        z = None
        break
    else:
        n.append(int(x))
        m.append(y)
        correct.append(z)
amount = 0
sum = 0
for i in range(len(correct)):
    if correct[i] == "right":
        amount+=1
        var = m[i]
        for j in range(len(m)):
            if m[j] == var:
                if correct[j]== "wrong":
                    sum+=20
        sum+=n[i]
print(amount, sum)
