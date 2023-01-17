"""
Тимофей записал два числа в двоичной системе счисления и попросил
Гошу вывести их сумму, также в двоичной системе. Встроенную в язык
программирования возможность сложения двоичных чисел применять нельзя.
Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов
максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке.
Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления."""


n_1 = input().strip()
n_2 = input().strip()
result = []
k = 0

if len(n_1) > len(n_2):
    m = len(n_1) - len(n_2)
    n_2 = n_2.zfill(len(n_1))
    # n_2 += [0] * m
elif len(n_2) > len(n_1):
    m = len(n_2) - len(n_1)
    n_1 = n_1.zfill(len(n_2))
    # n_1 += [0] * m

num_1 = list(map(int, n_1[::-1]))
num_2 = list(map(int, n_2[::-1]))

l = len(num_1)
for i in range(l):
    if k + num_1[i] + num_2[i] == 0:
        result.append(0)
        k = 0
    elif k + num_1[i] + num_2[i] == 1:
        result.append(1)
        k = 0
    elif k + num_1[i] + num_2[i] == 2:
        result.append(0)
        k = 1
    else:
        result.append(1)
        k = 1
if k == 1:
    result.append(1)

result = result[::-1]
print(int(''.join(str(x) for x in result)))
print(n_1, n_2)
