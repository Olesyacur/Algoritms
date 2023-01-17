from typing import List, Tuple

def moving_average(street: List[int], n: int) -> List[int]:
    #n, street = read_input()
    distance = []
    free = None
    for i, place in enumerate(street):
        if place == 0:
            free = i
            distance.append(0)
            continue
        if (place != 0 and free != None):
            distance.append(i - free)
        else:
            distance.append(n)
    free = None
    for i, place in reversed(list(enumerate(street))):
        if place == 0:
            free = i
            continue
        if (place != 0 and free != None and distance[i] > free - i):
            distance[i] = (free - i)
    return(distance)

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    street = list(map(int, input().split()))
    return street, n

street, n = read_input()
print(" ".join(map(str, moving_average(street, n))))