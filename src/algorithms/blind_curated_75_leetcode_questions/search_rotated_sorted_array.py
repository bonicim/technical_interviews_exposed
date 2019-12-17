def search(nums, target):
    def find_rotation_point(nums):
        if nums[0] < nums[len(nums) - 1]:
            return 0

        if len(nums) == 1:
            return 0

        left = 0
        right = len(nums) - 1
        leftmost = nums[0]

        while left < right:
            midpoint_index = left + ((right - left) // 2)
            midpoint = nums[midpoint_index]
            if midpoint >= leftmost:
                left = midpoint_index
            elif midpoint < leftmost:
                right = midpoint_index
            if right - left == 1:
                return right

    def binary_search(nums, left_index, right_index, target):
        while left_index <= right_index:
            midpoint_index = left_index + ((right_index - left_index) // 2)
            midpoint = nums[midpoint_index]

            if target == midpoint:
                return midpoint_index
            if target < midpoint:
                right_index = midpoint_index - 1
            else:
                left_index = midpoint_index + 1

        return -1

    if not nums:
        return -1
    rotation_point_index = find_rotation_point(nums)

    if nums[rotation_point_index] == target:
        return rotation_point_index

    if rotation_point_index == 0:
        return binary_search(nums, rotation_point_index, len(nums) - 1, target)

    if target < nums[0]:
        return binary_search(nums, rotation_point_index, len(nums) - 1, target)
    return binary_search(nums, 0, rotation_point_index, target)
