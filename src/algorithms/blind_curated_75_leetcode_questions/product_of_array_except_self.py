def product_except_self(nums):
    """
    Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Note: Please solve it without division and in O(n).

    Follow up:
    Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
    """
    # return brute_force(nums)
    # return greedy_approach_sub_optimal_space_complexity(nums)
    return greedy_approach_optimal_space_complexity(nums)


def brute_force(nums):
    products = [1] * len(nums)

    for index in range(len(nums)):
        for inner_index, other_num in enumerate(nums):
            if index != inner_index:
                products[index] = products[index] * other_num

    return products


def greedy_approach_sub_optimal_space_complexity(nums):
    products_except_self = [1] * len(nums)

    products_before_index = [1] * len(nums)
    product_before_current_index = 1
    for index, current_num in enumerate(nums):
        products_before_index[index] = product_before_current_index
        product_before_current_index = product_before_current_index * current_num

    products_after_index = [1] * len(nums)
    product_after_current_index = 1
    for index in range(len(nums) - 1, -1, -1):
        products_after_index[index] = product_after_current_index
        product_after_current_index = product_after_current_index * nums[index]

    for index in range(len(products_except_self)):
        products_except_self[index] = (
            products_before_index[index] * products_after_index[index]
        )

    return products_except_self


def greedy_approach_optimal_space_complexity(nums):
    products_before_index = [1] * len(nums)
    product_before_current_index = 1
    for index, current_num in enumerate(nums):
        products_before_index[index] = product_before_current_index
        product_before_current_index = product_before_current_index * current_num

    products_except_self = [1] * len(nums)
    product_after_current_index = 1

    for index in range(len(nums) - 1, -1, -1):
        products_except_self[index] = (
            products_before_index[index] * product_after_current_index
        )
        product_after_current_index = product_after_current_index * nums[index]

    return products_except_self
