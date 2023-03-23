n= input().split()
for i in n:
    i = int(i)
standard = [1, 1, 2, 2, 2, 8]
answer=[]
for i in range(len(standard)):
    if int(n[i]) > standard[i]:
        answer.append(standard[i]-int(n[i]))
    elif int(n[i]) < standard[i]:
        answer.append(standard[i]-int(n[i]))
    else:
        answer.append(0)
for i in answer:
    print(i, end = " ")