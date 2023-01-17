# ID успешной посылки 73836018

k = int(input())
matrix = ''.join(input() for i in range(4))

line = list(matrix.replace('.', ''))

bonus = 0
for i in range(10):
    j = str(i)
    count =int(line.count(j))
    if count <= k*2 and count != 0:
        bonus += 1

print(bonus)