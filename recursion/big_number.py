'''Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.'''


def comparator_number(number_1, number_2):  # функция-компаратор
    return number_1 > number_2

def biggest_number(array, less):

    for i in range(1, len(array)):
        item_to_sort = array[i]
        j = i
        while j > 0 and less(
                item_to_sort + array[j - 1],
                array[j - 1] + item_to_sort
                ):
          array[j - 1], array[j] = array[j], array[j - 1]
          j -= 1
    print(''.join(array))

if __name__ == '__main__':
   n = int(input())
   line = list(input().split())
   biggest_number(line, comparator_number)
