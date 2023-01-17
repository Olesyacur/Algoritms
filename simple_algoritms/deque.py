'''
Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x), pop_back(),
pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись за
O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее
100000. Во второй строке записано число m — максимальный размер дека. Он не
превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится
максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится
максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то
вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст,
то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных
запросов push_back(x) и push_front(x) ничего выводить не надо.'''


# ID 75482937

class DequeError(Exception):
    """Пустой или переполненный deque."""
    pass


class Deque:

    def __init__(self, n):
        self.__deque = [None] * max_size
        self.__max = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__max

    def __get_index(self, method):
        if method == 'push_back':
            return (self.__tail + 1) % self.__max
        if method == 'push_front':
            return (self.__head - 1 + self.__max) % self.__max
        if method == 'pop_back':
            return (self.__tail - 1 + self.__max) % self.__max
        if method == 'pop_front':
            return (self.__head + 1) % self.__max

    def push_back(self, number):
        if self.is_full():
            raise DequeError('error')
        self.__deque[self.__tail] = number
        self.__tail = self.__get_index('push_back')
        self.__size += 1

    def push_front(self, number):
        if self.is_full():
            raise DequeError('error')
        self.__head = self.__get_index('push_front')
        self.__deque[self.__head] = number
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise DequeError('error')
        number = self.__deque[self.__tail-1]
        self.__tail = self.__get_index('pop_back')
        self.__size -= 1
        return number

    def pop_front(self):
        if self.is_empty():
            raise DequeError('error')
        number = self.__deque[self.__head]
        self.__head = self.__get_index('pop_front')
        self.__size -= 1
        return number


if __name__ == '__main__':
    command_count = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(command_count):
        try:
            command, *args = input().split()
            answer = getattr(deque, str(command))(*args)
            if answer:
                print(answer)
        except DequeError:
            print('error')
