# ID 77867299

def partition(participants, left, right):
    pivot = left

    for i in range(left, right):
        if participants[i] < participants [right]:
            participants[i], participants[pivot] = participants[pivot], participants[i]
            pivot += 1

    participants[pivot], participants[right] = participants[right], participants[pivot]
    return pivot

def quicksort(participants, left, right):
    if left < right:
        pivot = partition(participants, left, right)
        quicksort(participants, left, pivot - 1)
        quicksort(participants, pivot + 1, right)

def sort_type(participants):
    participants[1] = - int(participants[1])
    participants[2] = int(participants[2])
    return [participants[1], participants[2], participants[0]]

if __name__ == '__main__':
    count_participants = int(input())
    participants = [
            sort_type(input().split()) for _ in range(count_participants)
    ]
    left = 0
    right = len(participants)
    quicksort(participants, left, right - 1)
    print('\n'.join([player[2] for player in participants]))
