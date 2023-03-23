store=[]
for i in range(5):
    sum =0
    score= input().split()
    for i in score:
        i= int(i)
        sum+=i
    store.append(sum)
max = store[0]
place = 1
for i in range(len(store)):
    if store[i]>max:
        max = store[i]
        place = i + 1
print(place, max)
