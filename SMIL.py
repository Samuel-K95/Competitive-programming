x=input()
for i in range(len(x)):
    if i+1<len(x):
        if x[i] + x[i + 1] == ":)" or x[i] + x[i + 1] == ";)":
            print(i)
        elif i+2<len(x)-1:
            if x[i] + x[i+1]+ x[i+2] == ":-)" or x[i] + x[i+1] + x[i+2] == ";-)":
                print(i)