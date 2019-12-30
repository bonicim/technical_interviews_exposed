def find_missing_integer_ii(nums):
    """Given a list of unsorted, distinct, contiguous integers, return the value of the missing integer that would
    make the list fully contiguous. The list contains only non-negative integers.

    Example:  [ 2, 3, 0] => 1
    """
    # return sorted_solution(nums)
    # return hash_set_solution(nums)
    return triangular_series_solution(nums)


def sorted_solution(nums):
    sorted_nums = sorted(nums)

    for index, num in enumerate(sorted_nums):
        if index != num:
            return index

    return len(nums)


def hash_set_solution(nums):
    nums_temp = set(nums)

    for index in range(len(nums)):
        if index not in nums_temp:
            return index

    return len(nums)


def triangular_series_solution(nums):
    """
    For more on this mathematical property, see https://www.interviewcake.com/concept/java/triangular-series
    """
    nums_sum = sum(nums)
    num_length = len(nums)
    triangular_sum = (num_length ** 2 + num_length) // 2
    return triangular_sum - nums_sum
