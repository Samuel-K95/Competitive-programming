first =[]
second=[]
ans=[]
for i in range(3):
    x, y= input().split()
    first.append(int(x))
    second.append(int(y))
for i in range(len(first)):
    count = 0
    for j in range(len(first)):
        if i == j:
            continue
        else:
            if first[i]== first[j]:
                count+=1
    if count< 1:
        ans.append(first[i])
for i in range(len(second)):
    count = 0
    for j in range(len(second)):
        if i == j:
            continue
        else:
            if second[i]== second[j]:
                count+=1
    if count< 1:
        ans.append(second[i])
for i in ans:
    print(i, end =" ")
