def binary_search(arr, low, high, target):
    if low == high:
        return arr[low] == target

    while low < high:
        midpoint_index = low + ((high - low) // 2)
        midpoint = arr[midpoint_index]

        if midpoint == target:
            return True

        if midpoint < target:
            low = midpoint + 1
        else:
            high = midpoint - 1

    return False
