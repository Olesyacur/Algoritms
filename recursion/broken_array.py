  #ID 78213049
"""
Задача.
Отсортированные по возрастанию данные из кольцевого буфера скопированы
в обычный массив, но сдвинуты относительно исходной отсортированной
последовательности.
Необходимо обеспечить возможность находить в полученном массиве нужный
элемент за O(logn).
В массиве только уникальные элементы.

Параметры ввода:
Функция принимает массив натуральных чисел, длиной не более 10000 и
искомое число.
Элементы массива и искомое число не превосходят по значению 10000.

Параметры вывода:
Необходимо вернуть искомого элемента или, при его отсутствии,
вернуть -1.
"""


def broken_search(nums, target) -> int:
    if len(nums) == 0:
        return -1
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def test() -> None:
    arr: list[int] = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
