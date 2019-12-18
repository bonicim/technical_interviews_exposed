def product(nums):
    """
    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

    Example 1:

    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    Example 2:

    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    """
    # return kadane_algorithm_solution(nums)
    return dynamic_programming_solution(nums)


def kadane_algorithm_solution(nums):
    max_prod_ending = nums[0]
    min_prod_ending = nums[0]
    max_so_far = nums[0]

    for index in range(1, len(nums)):
        current_num = nums[index]
        temp_max = max_prod_ending

        max_prod_ending = max(
            current_num, current_num * max_prod_ending, current_num * min_prod_ending
        )
        min_prod_ending = min(
            current_num, current_num * temp_max, current_num * min_prod_ending
        )

        max_so_far = max(max_so_far, max_prod_ending)

    return max_so_far


def dynamic_programming_solution(nums):
    max_prods = [0] * len(nums)
    min_prods = [0] * len(nums)
    max_result = nums[0]
    max_prods[0] = nums[0]
    min_prods[0] = nums[0]

    for index in range(1, len(nums)):
        current_num = nums[index]
        previous = index - 1

        if current_num < 0:
            max_prods[index] = max(current_num, current_num * min_prods[previous])
            min_prods[index] = min(current_num, current_num * max_prods[previous])
        else:
            max_prods[index] = max(current_num, current_num * max_prods[previous])
            min_prods[index] = min(current_num, current_num * min_prods[previous])

        max_result = max(max_result, max_prods[index])

    return max_result
