'''Астрологи объявили день очередей ограниченного размера. Тимофею нужно
написать класс MyQueueSized, который принимает параметр max_size, означающий
максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой
очереди. Функции, которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит
5000.
Во второй строке задан максимально допустимый размер очереди, он не

Далее идут команды по одной на строке. Команды могут быть следующих видов:


push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове
операций pop() или peek() для пустой очереди нужно вывести «None».
Формат вывода
Напечатайте результаты выполнения нужных команд, по одному на строке.'''


class QueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max = n
        self.head = 0
        self.tail = 0
        self.rate = 0


    def is_empty(self):
        return self.rate == 0

    def push(self, x):
        if self.rate != self.max:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max
            self.rate += 1
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return 'None'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max
        self.rate -= 1
        return x

    def peek(self):
        if self.is_empty():
            return 'None'
        return self.queue[self.head]

    def size(self):
        return self.rate

if __name__ == '__main__':
    lot = int(input())
    n = int(input())
    queue = QueueSized(n)
    for index in range(lot):
        command, *x = input().split()
        answer = getattr(queue, str(command))(*x)
        if command == 'pop' or command == 'peek' or command == 'size':
            print(answer)
        elif answer == 'error' or answer == 'None':
            print(answer)
        else:
            index += 1
