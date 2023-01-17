'''
Найти две различные строки, которые для заданной хеш-функции
будут давать одинаковое значение.
a = 1000 и m = 123 987 123.
Необходимо использовать в качестве значений отдельных символов их коды
в таблице ASCII.
'''

import random
import string

a = 1000
m = 123987123


def polinom(a, mod, string):
    hash = 0
    degree_q = 1
    for elem in string:
        hash = ((hash + ord(elem) * degree_q) % mod)
        degree_q = (degree_q * a) % mod
    return int(hash)


str_in = string.ascii_lowercase
str = ''.join(random.choice(str_in) for i in range(10))
h = polinom(a, m, str[::-1])

d_res = {}

while True:
    str = ''.join(random.choice(str_in) for i in range(10))
    h = polinom(a, m, str[::-1])
    if h in d_res.keys() and d_res[h] != str:
        print(d_res[h])
        print(str)
        break
    else:
        d_res[h] = str
    if len(d_res) == m:
        break
