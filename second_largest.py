'''n = int(input())
ans=[]
final=[]
for i in range(n):
    a,b,c = input().split()
    ans.append(int(a))
    ans.append(int(b))
    ans.append(int(c))
    min = ans[0]
    if ans[0]<int(b) and ans[0]<int(c):
        min = ans[0]
    elif ans[1]<int(a) and ans[1]<int(c):
        min = ans[1]
    else :
        min = ans[2]
    max = ans[0]
    if ans[0]>int(b) and ans[0]>int(c):
        max = ans[0]
    elif ans[1]>int(a) and ans[1]>int(c):
        max = ans[1]
    else :
        max = ans[2]
    for i in range(len(ans)):
        if ans[i] == max:
            continue
        elif ans[i] == min:
            continue
        else:
            print(ans[i])
            break'''
n = int(input())
print(float(n/4))


