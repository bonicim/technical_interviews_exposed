"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""


def two_sum_sorted_array(numbers, target):
    return two_sum_sorted_array_v1(numbers, target)


def two_sum_sorted_array_v1(numbers, target):
    left_side = 0
    right_side = len(numbers) - 1

    while left_side < right_side:
        sum = numbers[left_side] + numbers[right_side]

        if sum == target:
            return left_side + 1, right_side + 1

        if sum < target:
            left_side += 1
        else:
            right_side -= 1

    raise LookupError(
        "Solution incorrectly implemented. Should always return a tuple of two indexes."
    )


def two_sum_sorted_array_v2(numbers, target):
    def binary_search(left, right, target, numbers):
        while left < right:
            mid = (left + right) // 2
            current_num = numbers[mid]

            if current_num < target:
                left = mid + 1

            elif current_num > target:
                right = mid
            else:
                if numbers[mid - 1] == target:
                    return mid
                elif numbers[mid + 1] == target:
                    return mid + 1
                right = mid

        if left == right and numbers[left] == target:
            return left
        return -1

    for index, number in enumerate(numbers):
        complement = target - number
        other_index = binary_search(index, len(numbers) - 1, complement, numbers)

        if other_index != -1:
            return index + 1, other_index + 1

    raise LookupError(
        "Solution incorrectly implemented. Should always return a tuple of two indexes."
    )
