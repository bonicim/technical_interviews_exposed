def get_index_equals_value(nums):
    return binary_search_solution(nums, 0, len(nums) - 1, -1)


def binary_search_solution(nums, start, end, current_min_index):
    if not nums:
        return -1

    if start == end:
        if start == 0:
            if nums[start] == 0:
                return start
            else:
                return current_min_index

        if nums[end] == end:
            return end
        else:
            return current_min_index

    mid = (end - start) // 2
    if mid == 0:
        mid = start

    # search left
    if nums[mid] > mid:
        return binary_search_solution(nums, start, mid - 1, current_min_index)

    # search right
    if nums[mid] < mid:
        return binary_search_solution(nums, mid + 1, end, current_min_index)

    if nums[mid] == mid:
        return binary_search_solution(nums, start, mid - 1, mid)
