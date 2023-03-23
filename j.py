x=int(input())
num =[]
for i in range(x):
    n = int(input())
    num.append(n)
for i in num:
    if i%2 == 0:
        print(i ,"is even")
    else:
        print( i , "is odd")

