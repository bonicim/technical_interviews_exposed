def search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) -1

    while left <= right:
        pivot_idx = (right + left) // 2
        guess = nums[pivot_idx]

        if guess == target:
            return pivot_idx

        # check if we are in left-sorted portion
        if nums[left] <= guess:
            

            if target < nums[left]:
                left = pivot_idx + 1
            if target > guess or target < nums[left]:
                # search right
                left = pivot_idx + 1
            else:
                # target is in left-sorted portion of the array
                # search right
                right = pivot_idx - 1
        else:
            # right-sorted portion
            if target > guess and target > nums[right]:
                right = pivot_idx -1
            elif target < guess or
            else:
                # search the right portion
                left = pivot_idx + 1
                
    return -1 
    
        
def search_old(nums, target):
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
