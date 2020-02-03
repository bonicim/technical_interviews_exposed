"""
    Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Note: Please solve it without division and in O(n).

    Follow up:
    Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

"""Commentary

The key to solving this problem elegantly and the most efficient way (n runtime but at a cost of n space) is to recognize
that the the product of all numbers except the current number is the same thing as saying: give me the product of the product
of numbers left of the current number and right of the current number. Visually, you can see this:

Array
4, 5, 8, 2

Product of numbers left of each box
1, 1*4, 1*4*5, 1*4*5*8

Product of numbers right of each box
1*8*2*5, 1*8*2, 1*8, 1

Then we multiply both arrays to give us the complete answer.

To arrive at the efficient solution is not intuitive. A technique to understanding the efficient solution is to
draw out an example of what the product of each number is supposed to look like. By drawing out the example, we can
get or at least glimpse the solution of using left and right total products.

The implementation simply follows that logic.
"""


def product_except_self(nums):

    # return brute_force(nums)
    return greedy_approach_sub_optimal_space_complexity(nums)
    # return greedy_approach_optimal_space_complexity(nums)


def brute_force(nums):
    products = [1] * len(nums)

    for index in range(len(nums)):
        for inner_index, other_num in enumerate(nums):
            if index != inner_index:
                products[index] = products[index] * other_num

    return products


def greedy_approach_sub_optimal_space_complexity(nums):
    product_left_of_index = [1] * len(nums)
    current_product_left_of_index = 1
    for index, current_num in enumerate(nums):
        product_left_of_index[index] = current_product_left_of_index
        current_product_left_of_index = current_product_left_of_index * current_num

    product_right_of_index = [1] * len(nums)
    current_product_right_of_index = 1
    for index in range(len(nums) - 1, -1, -1):
        product_right_of_index[index] = current_product_right_of_index
        current_product_right_of_index = current_product_right_of_index * nums[index]

    # using list comprehension to simplify the multiplication of two arrays of the same size
    return [x * y for x, y in zip(product_left_of_index, product_right_of_index)]


def greedy_approach_optimal_space_complexity(nums):
    product_left_of_index = [1] * len(nums)
    current_product_left_of_index = 1
    for index, current_num in enumerate(nums):
        product_left_of_index[index] = current_product_left_of_index
        current_product_left_of_index = current_product_left_of_index * current_num

    products_except_self = [1] * len(nums)
    current_product_right_of_index = 1
    for index in range(len(nums) - 1, -1, -1):
        products_except_self[index] = (
            product_left_of_index[index] * current_product_right_of_index
        )
        current_product_right_of_index = current_product_right_of_index * nums[index]

    return products_except_self
