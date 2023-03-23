n = input()
x = (len(n)/2)
if len(n)%2 != 0:
    print("fix")
else:
    if n[int(x)-1] == '(' and n[int(x)] == ')':
        print("correct")
    else:
        print("fix")