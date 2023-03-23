word = input()
lower =['a','e','i','o','u']
upper =['A','E','I','O','U']
count=0
for i in range(len(word)):
    if word[i] in lower or word[i] in upper:
        count+=1
    else:
        continue
print(count)