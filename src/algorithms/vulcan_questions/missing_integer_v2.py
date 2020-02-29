def missing_integer_v2(arr, k):
    # this is very unintuitive way of checking if the distance between the current number and the number ahead is greater than or equal to 2 spots
    # if we find that somewhere in the middle of the array that there is a missing integer that should be in the realm of 1...end of the list
    # then regardless of what K is, which will always be positive, we will know that there is a missing integer in the sorted array
    for index in range(len(arr) - 1):
        curr = arr[index] + 1
        ahead = arr[index + 1]
        if curr < ahead:
            return False

    # this section checks for the cases in which the sorted array begins with 0 or numbers greater than 1
    first = arr[0]
    last = arr[len(arr) - 1]

    # if the array starts with 2 or greater, we'll never have a series starting with 1
    if first > 1:
        return False

    # this is the case where the series starts with 0 and has no duplicates
    # for such a series, k must be equal to less than the size of the array minus 1
    # this checks for the ideal series: ex 0,1,2,3,4,5
    if first == 0:
        if k > len(arr) - 1:
            return False
        if k == len(arr) - 1 and last != k:
            return False
        if k < len(arr) - 1 and last < k:
            return False

    return True
