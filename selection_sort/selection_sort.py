def find_lowest(arr: list):
    lowest = arr[0]
    lowest_index = 0

    for i in range(len(arr)):
        if arr[i] < lowest:
            lowest = arr[i]
            lowest_index = i

    return lowest, lowest_index


def selection_sort(arr: list, new_arr: list = []):

    # [] or [23] returns
    if len(arr) <= 1:
        return new_arr

    # if [1, 2] returns
    if len(arr) <= 2 and arr[0] < arr[1]:
        return new_arr

    lowest, lowest_index = find_lowest(arr)
    new_arr.append(lowest)
    arr.pop(lowest_index)

    return selection_sort(arr=arr, new_arr=new_arr)


if __name__ == "__main__":
    arr = [99, 29, 92, 2, 21, 35, 15, 87, 11, 70, 56, 69, 20, 8, 1, 55, 23,
           61, 16, 20, 58, 91, 39, 33, 84, 6, 53, 40, 76, 24, 36, 44, 34,
           96, 52, 27, 77, 18, 57, 3, 18, 47, 7, 43, 12, 8, 54, 99, 34, 36,
           10, 14, 96, 82, 30, 57, 4, 66, 48, 9, 39, 81, 42, 16, 28, 1, 79,
           55, 6, 9, 55, 65, 40, 2, 61, 61, 19, 76, 26, 78, 35, 48, 37, 47,
           42, 86, 1, 47, 49, 56, 52, 33, 84, 2, 52, 79, 51, 79, 24, 22]

    v = selection_sort(arr=arr.copy())
    arr.sort()
    print(v == arr)
    print(v)
