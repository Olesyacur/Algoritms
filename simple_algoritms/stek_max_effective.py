'''
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1). Для
пустого стека операция должна возвращать None. При этом push(x) и pop() также
должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
100000. Далее идут команды по одной в строке. Команды могут быть следующих
видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для
команды pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек
пустой, для команды get_max() напечатайте «None». Если происходит удаление из
 пустого стека — напечатайте «error».'''



class Stack:
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        if self.items == [] or int(item) > self.max_items[len(self.items)-1]:
            self.max_items.append(int(item))
        else:
            self.max_items.append(self.max_items[len(self.items)-1])
        self.items.append(int(item))

    def pop(self):
        if self.items == []:
            return('error')
        self.max_items.pop()
        self.items.pop()

    def get_max(self):
        if self.items == []:
            return None
        return self.max_items[len(self.items) - 1]

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
