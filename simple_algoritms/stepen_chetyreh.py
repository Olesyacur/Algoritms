"""
Напишите программу, которая определяет, будет ли положительное целое
число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое
неотрицательное число.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –—
в обратном случае."""


n = int(input())
if n == 1:
    print('True')
while n >= 4:
    m = n // 4
    if n % 4 != 0:
        print('False')
        break
    elif n == 4:
        print('True')
        break
    else:
        n = m
if n < 4 and n != 1:
    print('False')
