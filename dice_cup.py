n, m = input().split()
n= int(n)
m = int(m)
val=[]
count=[]
answer=[]
if n>m:
    min =m
else:
    min=n
for i in range(n+1):
    for j in range(m+1):
        if i==0 or j==0:
            continue
        else:
            sum = i+j
            if sum > min:
                val.append(sum)
for i in range(len(val)):
    count.append(1)
for i in range(len(val)):
    for j in range(len(val)):
        if i == j:
            continue
        elif val[i] == val[j]:
            count[i]+=1
max = count[0]
for i in range(len(count)):
    if count[i]>max or count[i] == max:
        if val[i] in answer:
            continue
        else:
            answer.append(val[i])
for i in answer:
    print(i)










