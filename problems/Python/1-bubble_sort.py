# Bubble sort
from typing import List


def swap(arr: List, index: int) -> None:
    arr[index], arr[index+1] = arr[index+1], arr[index]


def bubble_sort(arr: List) -> None:
    for i in range(len(arr)):
        for index, elem in enumerate(arr[:-1]):
            if elem > arr[index + 1]:
                swap(arr, index)


if __name__ == "__main__":
    arr = [21, 3, 1, 4, 5, 6]
    arr2 = arr[:]
    bubble_sort(arr)
    arr2 = sorted(arr2)
    assert arr, arr2
    print(arr == arr2)
