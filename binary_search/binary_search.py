def binary_search(arr: list, value: int, high: int, low: int = 0) -> int | None:

    if low > high:
        return None

    middle = int((high + low) / 2)
    middle_value = arr[middle]

    if middle_value == value:
        return middle

    if middle_value > value:
        high = middle - 1

    if middle_value < value:
        low = middle + 1

    return binary_search(arr=arr, value=value, high=high, low=low)


if __name__ == "__main__":

    arr = [99, 29, 92, 2, 21, 35, 15, 87, 11, 70, 56, 69, 20, 8, 1, 55, 23,
           61, 16, 20, 58, 91, 39, 33, 84, 6, 53, 40, 76, 24, 36, 44, 34,
           96, 52, 27, 77, 18, 57, 3, 18, 47, 7, 43, 12, 8, 54, 99, 34, 36,
           10, 14, 96, 82, 30, 57, 4, 66, 48, 9, 39, 81, 42, 16, 28, 0, 79,
           55, 6, 9, 55, 65, 40, 2, 61, 61, 19, 76, 26, 78, 35, 48, 37, 47,
           42, 86, 0, 47, 49, 56, 52, 33, 84, 2, 52, 79, 51, 79, 24, 22]

    random_value_that_exists = 4
    random_value_that_not_exists = 10101010

    arr.sort()

    v1 = binary_search(arr=arr,
                       value=random_value_that_exists,
                       high=len(arr) - 1,
                       low=0)
    print(v1)

    v2 = binary_search(arr=arr,
                       value=random_value_that_not_exists,
                       high=len(arr) - 1,
                       low=0)
    print(v2)
