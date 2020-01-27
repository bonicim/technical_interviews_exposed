# this a modified version of quicksort, which sorts in-place an array of integers, but only the side
# of the integers that are part of the range up to the target_index
def quicksearch(arr, low, high, target_index):
    if low < high:
        partition_index = partition(arr, low, high)
        if partition_index == target_index:
            return
        # if the partition index is less than the target index, we know that everything less
        # than the partition_index is in the right place
        # however, the target index is greater than the partition index, which means that
        # there could be, most likely, some elements that are still not sorted in the range from partition index to high
        # in other words, we only want to sort the side up to the target index
        if partition_index < target_index:
            quicksearch(arr, partition_index + 1, high, target_index)
        else:
            # in this case, everything is sorted to the right of the partition index, but the target index is less
            # than the partition index, which means there still might be elements that are not sorted from the range low to target_index
            quicksearch(arr, low, partition_index - 1, target_index)


def partition(arr, low, high):
    pivot_index = get_pivot()
    swap(pivot_index, high)
    pivot = arr[high]
    border = low

    for index in range(low, high):
        if arr[index] < pivot:
            swap(arr, index, border)
            border += 1

    swap(arr, border, high)
