x=bin(int(input()))
y="0b"
for i in range(len(x)):
    if x[len(x)-1-i] =="b":
        break
    else:
        y+=str((x[len(x)-1-i]))
print(int(y,2))



