def three_product(nums):
    """
    Given a list of integers, find the highest product you can get from three of the integers.

    The input list_of_ints will always have at least three integers.
    """
    if len(nums) < 3:
        return ValueError("List of numbers must have at least three numbers")

    highest_product = nums[0] * nums[1] * nums[2]
    highest_product_of_2 = nums[0] * nums[1]
    highest = nums[0]
    lowest_product_of_2 = nums[0] * nums[1]
    lowest = nums[0]

    for index in range(2, len(nums)):
        current_num = nums[index]

        highest_product = max(
            highest_product,
            current_num * highest_product_of_2,
            current_num * lowest_product_of_2,
        )

        highest_product_of_2 = max(highest_product_of_2, highest * current_num)
        lowest_product_of_2 = min(lowest_product_of_2, lowest * current_num)

        highest = max(highest, current_num)
        lowest = min(lowest, current_num)

    return highest_product
