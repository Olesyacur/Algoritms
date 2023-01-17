'''На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.
Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не
превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.'''


def comby_letter_button(prefix):
    LETTERS = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }

    def comby_letter(prefix, item, result):
        if prefix == '':
           result.append(item)
           return
        for letter in LETTERS[prefix[0]]:
            item += letter
            comby_letter(prefix[1:], item, result)
            item = item[:-1]
    result = []
    comby_letter(prefix, '', result)
    for res in result:
        print(res, end=' ')

if __name__ == '__main__':
    string = input()
    comby_letter_button(string)
    