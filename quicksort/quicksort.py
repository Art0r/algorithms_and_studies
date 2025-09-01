import random


def quicksort(arr: list):

    if len(arr) <= 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr

    pivot = round(len(arr) / 2)
    left = list(filter(lambda x: x < arr[pivot], arr))
    right = list(filter(lambda x: x > arr[pivot], arr))
    middle = list(filter(lambda x: x == arr[pivot], arr))

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":

    arr = [random.randint(0, 99) for i in range(100)]

    sorted_arr = quicksort(arr.copy())
    print(sorted_arr == sorted(arr))
