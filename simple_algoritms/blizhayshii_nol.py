n = int(input())
street = list(map(int, input().split()))


free = []
free = [[int(f) if p == 0 else None for p in street] for f in range(n)]
#for f in range(n):
    #if street[f] == 0:
        #free.append(f)

distan = []
matrix = []
for i, place in enumerate(free):
    for j in range(n):
        if j != place:
            k = j - place
            distan.append(abs(k))
        else:
            distan.append(0)

matrix = [distan[i:i+n] for i in range(0,len(distan),n)]
res=[]
for x in range(n):
    minimum = [min(i) for i in zip(*matrix)][x]
    res.append(minimum)

print(*res)
