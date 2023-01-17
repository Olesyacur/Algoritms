'''
Нужно определить длину наибольшей подстроки, которая не содержит повторяющиеся
символы.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит
10 000.

Формат вывода
Выведите натуральное число —– ответ на задачу.'''


def find_substrings(word):
    result = ''
    item = 0
    answer = 0
    while item <= (len(word) - 1):
        if word[item] not in result:
            result += word[item]
        else:
            result = result[result.index(word[item]) + 1:] + word[item]
        item += 1
        answer = max(answer, len(result))

    return answer


ans = find_substrings(str(input()))
print(ans)
