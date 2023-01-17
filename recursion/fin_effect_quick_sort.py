# ID 78285684
"""
Задача - определить победителя соревнования.
Каждый участник имеет уникальный логин. К нему привязаны два показателя:
количество решённых задач Pi и размер штрафа Fi.
Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Сортировать таблицу результатов следующим образом:
- первым идет тот, у которого решено больше задач;
- далее идёт участник с меньшим штрафом;
- далее у кого логин идёт раньше в алфавитном (лексикографическом) порядке.

Необходимо реализовать алгоритм быстрой сортировки.
Реализация сортировки не может потреблять O(n) дополнительной памяти для
промежуточных данных.

Параметры ввода:
Число участников n, 1 ≤ n ≤ 100 000.
В каждой n строке задана информация про одного из участников:
- уникальный логин (строкой из маленьких латинских букв длиной не более 20);
- число решённых задач Pi;
- штраф Fi.
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

Параметры вывода:
Для отсортированного списка вывести по порядку логины по одному в строке.
"""
class Participant:
    def __init__(self, name, points, fine) -> None:
        self.name = name
        self.points = points
        self.fine = fine

    def __str__(self):
        return self.name

    def __lt__(self, other) -> bool:
        if isinstance(other, Participant):
            return(
                (-self.points, self.fine, self.name) <
                (-other.points, other.fine, other.name)
            )
        return NotImplemented

def quicksort(participants, start=0, end=0) -> None:
    
    def partition(lo, hi) -> None:
        if lo >= hi:
            return
        left = lo
        right = hi
        pivot = participants[(left + right) // 2]

        while left <= right:
            while participants[left] < pivot:
                left += 1
            while pivot < participants[right]:
                right -= 1
            if left <= right:
                participants[left], participants[right] = participants[right], participants[left]
                left += 1
                right -= 1

        partition(lo, right)
        partition(left, hi)
    
    partition(start, end - 1)

if __name__ == '__main__':
    count_participants: int = int(input())
    participants = []
    for _ in range(count_participants):
        name, points, fine = input().split()
        participants.append(
            Participant(points=int(points), fine=int(fine), name=name)
        )
    
    start: int = 0
    end: int = len(participants)
    quicksort(participants, start, end)
    print(*participants, sep='\n')