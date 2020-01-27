def quicksort(arr, low, high):
    # sort only if there is more than one element in the array
    if low < high:
        # partition/sort the current array based on some partition
        partition_index = partition(arr, low, high)
        # sort the left side of the partition
        quicksort(arr, low, partition_index - 1)
        # sort the right side of the partition
        quicksort(arr, partition_index + 1, high)


# the work of quicksort is done in the partition function
def partition(arr, low, high):
    # choose some pivot
    pivot_index = generate_pivot_index(low, high)

    # move the value of the pivot to the far right or the box in the highest index
    swap(arr, pivot_index, high)
    pivot_index = high

    # set a pointer on the leftmost part of the array
    border = low

    for index in range(low, high):
        # depending on how you want to sort, change the logic in the if statement
        # depending on where you isolate the pivot value will determine your logic
        # if the pivot value is on the far right, then you want to operate/move elements that are less than the pivot
        # if the pivot value is on the far left, then you want to operate/move elements that are greater than the pivot
        if arr[index] < arr[pivot_index]:
            swap(arr, index, border)
            border += 1

    swap(arr, border, pivot_index)

    return border


def swap(arr, l, r):
    arr[l], arr[r] = arr[r], arr[l]


def generate_pivot_index(low, high):
    # implement any logic here
    return high
