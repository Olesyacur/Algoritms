'''
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции push
(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не
превосходит 10000. В следующих n строках идут команды. Команды могут быть
следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для
команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек
пустой, для команды get_max() напечатайте «None». Если происходит удаление из
пустого стека — напечатайте «error».'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if self.items == []:
            return('error')
        self.items.pop()

    def get_max(self):
        if self.items == []:
            return None
        return max(self.items)

if __name__ == '__main__':
    stack_max = Stack()
    n = int(input())
    for index in range(n):
        command, *item = input().split()
        answer = getattr(stack_max, str(command))(*item)
        if command == 'get_max':
            print(answer)
        elif answer == 'error':
            print('error')
        else:
            index += 1
