# merge sort


def merge(arr1: list, arr2: list) -> list:
    raise NotImplementedError
    len1, len2 = len(arr1), len(arr2)
    result = []
    for i in range(len1 + len2):
        result.append()


def merge_sort(arr: list) -> list:
    length = len(arr)
    if length == 1:
        return arr
    left = merge_sort(arr[:length//2])
    right = merge_sort(arr[length//2:])
    return merge(left, right)


if __name__ == "__main__":
    arr = [21, 3, 1, 4, 5, 6]
    arr2 = arr[:]
    merge_sort(arr)
    arr2 = sorted(arr2)
    assert arr, arr2
    print(arr == arr2)
