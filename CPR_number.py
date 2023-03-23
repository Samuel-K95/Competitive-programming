num = input()
val =[4,3,2,7,6,5,4,3,2,1]
c=0
sum=0
for i in num:
    if i == "-":
        continue
    else:
        sum+=(int(i)*val[c])
        c+=1
if sum%11 == 0:
    print(1)
else:
    print(0)


