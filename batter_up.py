x= int(input())
sum=0
ans=[]
num = input().split()
count =0
for i in num:
    if int(i)== -1:
        continue
    else:
        sum+=int(i)
        count+=1
print(sum/count)



