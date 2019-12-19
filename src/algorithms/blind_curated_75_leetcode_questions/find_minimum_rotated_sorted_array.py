def find_min(nums):
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the array.
    """
    if len(nums) == 1:
        return nums[0]

    if nums[len(nums) - 1] > nums[0]:
        return nums[0]

    first_num = nums[0]
    left = 0
    right = len(nums) - 1

    while left < right:
        pivot_index = left + ((right - left) // 2)
        pivot = nums[pivot_index]

        if pivot > first_num:
            left = pivot_index
        elif pivot < first_num:
            right = pivot_index

        if right - left == 1:
            return nums[right]
