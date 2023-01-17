'''
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если
очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.'''


class Queue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.rate = 0


    def is_empty(self):
        return self.rate == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.rate == 1 or self.rate == 2:
            deleted = self.head
            self.head = self.tail
            self.rate -= 1
            return deleted.value
        deleted = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.rate -= 1
        return deleted.value

    def put(self, x):
        if self.is_empty():
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.rate += 1

    def size(self):
        return self.rate

if __name__ == '__main__':
    lot = int(input())
    queue = Queue()
    for index in range(lot):
        command, *x = input().split()
        answer = getattr(queue, str(command))(*x)
        if command == 'get' or command == 'size':
            print(answer)
        else:
            index += 1
