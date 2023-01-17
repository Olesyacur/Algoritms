'''Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У
Васи есть копилка, в которую каждый день он может добавлять деньги (если,
конечно, у него есть такая финансовая возможность). В процессе накопления Вася
не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке
было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными
накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в
порядке неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда.
Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера
дня.'''


def day_buy(capital, cost, left, right):
    if right <= left != 0:
        return -1
    mid = (left + right) // 2
    if mid == 0 or capital[mid] >= cost > capital[mid - 1]:
        return mid + 1
    elif cost <= capital[mid]:
        return day_buy(capital, cost, left, mid)
    else:
        return day_buy(capital, cost, mid + 1, right)

if __name__ == '__main__':
    days = int(input())
    capital = list(map(int, input().split()))
    cost = int(input())
    possible_buy = []
    day_buy_1 = day_buy(capital, cost, left = 0, right = len(capital))
    possible_buy.append(day_buy_1)
    day_buy_2 = day_buy(capital, cost*2, left = 0, right = len(capital))
    possible_buy.append(day_buy_2)
    print(*possible_buy)
