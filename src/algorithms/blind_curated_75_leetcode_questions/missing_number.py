"""Given a list of unsorted, distinct, contiguous integers, return the value of the missing integer that would
make the list fully contiguous. The list contains only non-negative integers.

Example:  [ 2, 3, 0] => 1
"""

""" Commentary

To truly understand this problem, we have to recognize and understand the input. The input is a list of
unique numbers such that they can be arranged monotonically, save for one. For example, [3,1,0] is equiavalent
to [0,1,3], with 2 being the missing number. We can take advantage of this idea by using the indexes of the
array that hold these numbers. If we sorted the list, then we simply check the index agains the actual value for the missing number.

But if we didn't want to sort, we can use a set to store all the values of the list and then simply
iterate through all the index of the length of the list.

Finally, this problem alludes to the mathematical property of triangular sums, which can be used to
solve this problem very quickly.
"""


def find_missing_integer_ii(nums):

    # return sorted_solution(nums)
    # return hash_set_solution(nums)
    return triangular_series_solution(nums)


def sorted_solution(nums):
    sorted_nums = sorted(nums)

    for index, num in enumerate(sorted_nums):
        if index != num:
            return index

    # all the numbers from 0 to n-1 are present, so the missing number is simply the next
    # number in the serie
    # the edge case that this catches is [0,1,2]
    return len(nums)


def hash_set_solution(nums):
    nums_temp = set(nums)
    for index in range(len(nums)):
        if index not in nums_temp:  # allows for quick lookup
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
