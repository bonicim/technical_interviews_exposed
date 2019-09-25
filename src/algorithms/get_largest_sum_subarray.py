import math

"""
Given an array of integers, find the maximum sum of the largest, contiguous subarray
"""


def get_largest_sum_subarray(a):
    """ Returns the maximum sum of largest, contiguous subarray

    :param a: List of integers
    :returns: int
    :raises: None
    """
    # return brute_force(a)
    # return kadane_algorithm(a)
    # return dynamic_programming(a)
    return divide_and_conquer(a)


# Naive solution that runs in O(n^2)
def brute_force(a):
    if not a:
        return 0

    max_sum = a[0]
    for start_index, _ in enumerate(a):
        curr_sum = 0
        for current_end_index in range(start_index, len(a)):
            curr_sum = curr_sum + a[current_end_index]
            if curr_sum > max_sum:
                max_sum = curr_sum

    return max_sum


# Uses memoization to store the maximum subarray sums in a list
# Runs in 0(n) time and O(n) space
def dynamic_programming(a):
    if not a:
        return 0

    sub_array_sums = [None] * len(a)
    sub_array_sums[0] = a[0]
    max_sum = a[0]
    for index in range(1, len(a)):
        sum_at_index = sub_array_sums[index - 1] + a[index]
        index_val = a[index]
        if sum_at_index >= index_val:
            sub_array_sums[index] = sum_at_index
        else:
            sub_array_sums[index] = index_val
        if sub_array_sums[index] > max_sum:
            max_sum = sub_array_sums[index]

    return max_sum


# Kadane's algorithm runs in O(n)
# This algorithm is similar to the dynamic programming solution but with one crucial difference:
# it saves on space by setting a global variable for the current sum at an index and not saving all
# the subarray sums in a list
# https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
def kadane_algorithm(a):
    if not a:
        return 0

    max_sum = a[0]
    curr_sum = 0
    for num in a:
        curr_sum = num if curr_sum <= 0 else curr_sum + num
        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


# This algorithm uses the divide and conquer method by splitting the array in half
# and finding the maximum subarray of each half recursively
# We must also handle the case where the largest subarray could be in the middle
def divide_and_conquer(a):
    return max_sum_subarray(a, 0, len(a) - 1)


def max_sum_subarray(a, start, end):
    if not a:
        return 0
    if start == end:
        return a[start]

    mid = (start + end) // 2
    max_left_sum = max_sum_subarray(a, start, mid)
    max_right_sum = max_sum_subarray(a, mid + 1, end)
    max_middle_sum = max_middle_subarray(a, start, mid, end)

    return max(max_left_sum, max_right_sum, max_middle_sum)


def max_middle_subarray(a, start, mid, end):
    left_max_sum = a[mid]
    curr_left_sum = 0
    for index in range(mid, start - 1, -1):
        curr_left_sum = curr_left_sum + a[index]
        if curr_left_sum >= left_max_sum:
            left_max_sum = curr_left_sum

    right_max_sum = a[mid + 1]
    curr_right_sum = 0
    for index in range(mid + 1, end + 1):
        curr_right_sum = curr_right_sum + a[index]
        if curr_right_sum >= right_max_sum:
            right_max_sum = curr_right_sum

    return left_max_sum + right_max_sum
