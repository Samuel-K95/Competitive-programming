x = int(input())
answer = []
for i in range(x):
    alpha = {'a' : 0, 'b' : 0, 'c' : 0, 'd': 0, 'e': 0, 'f': 0, 'g' : 0, 'h' : 0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r' : 0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    flag = True
    word = input()
    for j in word:
        try:
            j = j.lower()
            alpha[j] += 1
        except:
            continue
        
    missing = "missing "
    for key, value in alpha.items():
        if value == 0:
            flag = False
            missing += key
    if flag:
        answer.append("pangram")
    else:
        answer.append(missing)
for i in answer:
    print(i)
