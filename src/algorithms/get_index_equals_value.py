def get_index_equals_value(nums):
    return binary_search_solution(nums, 0, len(nums) - 1)


def binary_search_solution(nums, start, end):
    if not nums:
        return -1

    if start == end:
        return -1

    if nums[start] == start:
        return start

    if nums[end] == end:
        return end

    mid = (end - start) // 2

    if nums[mid] < mid:
        return binary_search_solution(nums, mid, end)

    if nums[mid] == mid:
        return mid

    if nums[mid] > mid:
        return binary_search_solution(nums, start, mid)
