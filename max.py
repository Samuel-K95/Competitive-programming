n = int(input())
num = input().split()
for i in num:
    i = int(i)
min = num[0]
for i in range(len(num)):
    if num[i]< min:
        min = num[i]
print(min)