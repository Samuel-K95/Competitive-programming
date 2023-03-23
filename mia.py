ans =[]
while True:
    x = input().split()
    for i in x:
        i=int(i)
    if x == ['0','0','0','0']:
        break
    num1=[]
    num2=[]
    for i in range(len(x)):
       if i<2:
            num1.append(x[i])
       else:
           num2.append(x[i])
    if num1 == ['1','2'] or num1 == ['2','1']:
        ans.append("Player 1 wins.")
    elif num2 == ['1','2'] or num2 == ['2','1']:
        ans.append("Player 2 wins.")
    elif num1[0] == num1[1] and num2[0] == num2[1]:
        if num1 ==['6','6']:
            ans.append("Player 1 wins.")
        elif num2 ==['6','6']:
            ans.append("Player 2 wins.")
    elif num1[0] == num1[1]:
        ans.append("Player 1 wins.")
    elif num2[0] == num2[1]:
        ans.append("Player 2 wins.")
    else:
        if int(x[0]) > int(x[1]) and int(x[0]) == int(x[1]) :
            continue
        elif int(x[0]) < int(x[1]):
            x[0], x[1] = x[1], x[0]
        if int(x[2]) > int(x[3]) and int(x[2]) == int(x[3]):
            continue
        elif int(x[2]) < int(x[3]):
            x[2], x[3]= x[3], x[2]
        if (x[0], x[1]) == (x[2], x[3]):
            ans.append("Tie.")
    print(x)
for i in ans:
    print(i)

