n= int(input())
x = input().split()
y = input().split()
for i in x:
    if i not in y:
        print(i)