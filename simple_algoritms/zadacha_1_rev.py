#ID 74124718

from typing import List

def nearest_zero(street: List[int], n: int) -> List[int]:
    distance = [0] * n
    free = None
    for i, place in enumerate(street):
        if place == 0:
            free = i
            distance[i] == 0
            continue
        if (place != 0 and free is not None):
            distance[i] = i - free
        else:
            distance[i] = n
    free = None
    for i, place in list(enumerate(street))[::-1]:
        if place == 0:
            free = i
            continue
        if (free is not None and distance[i] > free - i):
            distance[i] = free - i
    return distance

def main() -> List[int]:
    n = int(input())
    street = [int(place) for place in input().split()]

    distance = nearest_zero(street, n)

    print(*distance)

if __name__ == '__main__':
    main()