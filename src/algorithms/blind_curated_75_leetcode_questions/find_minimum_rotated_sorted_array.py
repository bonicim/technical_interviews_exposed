def find_min(nums):
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the array.
    """

    res = nums[0]
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        # when the slice of the array is sorted, check the current result against the new minimum
        if nums[left] < nums[right]:
            res = min(res, nums[left])
            break
            
        pivot_index = (right + left) // 2
        pivot = nums[pivot_index]
        # the pivot is also our guess of the lowest number in the array; so check it against the current result 
        res = min(res, pivot)

        # the pivot is part of the sorted array on the right, so search left because the array on the left will have smaller values
        if pivot >= nums[left]:
            left = pivot_index + 1
        else:
        # the pivot is not part of the sorted array on the left, so search the right 
            right = pivot_index - 1

    return res


def find_min_pivot_index(nums):
    """
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    You may assume no duplicate exists in the array.
    """

    # handles case of a sorted array that shifted by 0
    if nums[len(nums) - 1] > nums[0]:
        return nums[0]

    left = 0
    right = len(nums) - 1
    rotate_index = 0

    while left < right:
        pivot_index = (right + left) // 2
        pivot = nums[pivot_index]

        if pivot >= nums[left]:
            left = pivot_index 
        else:
            right = pivot_index

        if right - left == 1:
            rotate_index = right
            break

    return nums[rotate_index]
