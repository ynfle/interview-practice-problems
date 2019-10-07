# Bubble sort
from typing import List


def swap(arr: List, index: int) -> None:
    arr[index], arr[index+1] = arr[index+1], arr[index]


def bubble_sort(arr: List) -> List:
    for i in range(len(arr)):
        for index, elem in enumerate(arr[:-1]):
            if elem > arr[index + 1]:
                swap(arr, index)
    return arr


if __name__ == "__main__":
    arr = [21, 3, 1, 4, 5, 6]
    sorted_arr = bubble_sort(arr)
    arr = sorted(arr)
    assert arr, sorted_arr
    print(arr == sorted_arr)
