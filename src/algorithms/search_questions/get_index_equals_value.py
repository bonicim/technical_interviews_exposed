# nums is always sorted
def get_index_equals_value(nums):
    return binary_search_solution_recursive(nums, 0, len(nums) - 1, -1)
    # return binary_search_iterative(nums)


# better solution because it's simple, fewer lines of code, and not recursive
def binary_search_iterative(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint_index = (left + right) // 2
        midpoint = arr[midpoint_index]
        # We have to check for 3 main cases: the index equals its value, the index is less than its value, and the index is greater than its value

        # If we found that the midpoint_index equals its value, we still have to check for three sub-cases:
        if midpoint_index == midpoint:
            # Sub-case 1: if the midpoint index is the first index, then it is lowest possible matching index which is the lowest possible index
            if midpoint_index == 0:
                return midpoint_index
            # Sub-case 2: if the immediate left is not the lowest possible matching index, we are on the lowest index
            if (
                midpoint_index == midpoint
                and midpoint_index - 1 - arr[midpoint_index - 1] != 0
            ):
                return midpoint_index
            # Sub-case 3: if the immediate left is the lowest possible matching index, we need to shrink the search space by eliminating everything to the right
            if (
                midpoint_index == midpoint
                and midpoint_index - 1 - arr[midpoint_index - 1] == 0
            ):
                right = midpoint_index - 1

        # The second main case means that the value is greater than the current index
        # in a sorted, monotonoically increasing array, this fact would hold true if we keep searching the rest of the elements to the right
        # thus there is no need to search the right
        # instead shrink the search space by shrinking the right side to the midpoint
        elif midpoint_index < midpoint:
            right = midpoint_index - 1

        # The final main case is the opposite of the previous case: the value at the index is less than the index itself
        # In a monotonically increasing array, all the values to the left would also be less than its index
        # example, [1,2,3]; at index 2, the value 3 is less than index 2. As we go left the index will always decrease by 1, moreover the value at the index will also decrease and the lowest it can decrease is by one. At best, the index and values at the index will decrease at the same rate of 1 as we go left. And if this middle point has shown that the value at the index is greater than the index, we can never find a situation in which the index equals its value if we keep searching left. Thus shrink the search space to the right
        else:
            left = midpoint_index + 1
    return -1


# Works, but too complicated, is recursive, and too many if statemnents and checks
def binary_search_solution_recursive(nums, start, end, current_min_index):
    if not nums:
        return -1

    # the lowest index matching is the first index, furthest left
    if start == end and start == 0 and nums[start] == 0:
        return start
    # the lowest index is not the first index and we are on the index that equals its value
    if start == end and start == 0:
        return current_min_index
    # we are in section where the first index is not within the current search space. the lowest index matching is the furthest right
    if start == end and nums[end] == end:
        return end
    if start == end:
        return current_min_index

    mid = (end - start) // 2
    if mid == 0:
        mid = start

    # search left
    if nums[mid] > mid:
        return binary_search_solution_recursive(nums, start, mid - 1, current_min_index)

    # search right
    if nums[mid] < mid:
        return binary_search_solution_recursive(nums, mid + 1, end, current_min_index)

    # search the first index if needed, search the immediate left of midpoint
    if nums[mid] == mid:
        return binary_search_solution_recursive(nums, start, mid - 1, mid)
