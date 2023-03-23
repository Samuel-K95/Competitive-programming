n = int(input())
if n%2 == 0:
    for i in range(n):
        for j in range(i+1):
            print("*"* n)
            break
else:
    c = 1
    for i in range(n):
        for j in range(i+1):
            print("*" * c, end = " ")
            c += 1
            break
        print("")


