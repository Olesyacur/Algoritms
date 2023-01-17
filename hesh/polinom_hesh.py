'''
Написать функцию, вычисляющую хеш строки s.
Необходимо использовать в качестве значений отдельных символов
их коды в таблице ASCII.

Формат ввода
Число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.
Число m (1 ≤ m ≤ 109) –— модуль.
Строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских
букв.

Формат вывода
Целое неотрицательное число –— хеш заданной строки.
'''


def polinom(basis, mod, string):
    hash = 0
    degree_q = 1
    for elem in string:
        hash = ((hash + ord(elem) * degree_q) % mod)
        degree_q = (degree_q * basis) % mod
    return int(hash)


basis = int(input())
mod = int(input())
string = input()

print(polinom(basis, mod, string[::-1]))
