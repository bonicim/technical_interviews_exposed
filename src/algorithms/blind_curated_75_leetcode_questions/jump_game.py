"""

"""


def can_jump(nums):
    return backtracking_solution(nums)


def backtracking_solution(nums):
    def can_jump_next_pos(pos, nums):
        if pos == len(nums) - 1:
            return True

        jump = min(len(nums) - 1, pos + nums[pos])

        # only jump from the next box as permitted by the smallest size of the allowable jump from the current box
        for next_pos in range(pos + 1, jump + 1):
            if can_jump_next_pos(next_pos, nums):
                return True

        return False

    return can_jump_next_pos(0, nums)


def top_down_dp_solution(nums):
    def can_jump_next_pos(pos, nums, cache):
        if cache[pos] is not None:
            return cache[pos]

        jump = min(len(nums) - 1, pos + nums[pos])

        for next_pos in range(pos + 1, jump + 1):
            if can_jump_next_pos(next_pos, nums, cache):
                cache[pos] = True
                return True

        cache[pos] = False
        return False

    cache = [None] * (len(nums))
    cache[len(nums) - 1] = True

    return can_jump_next_pos(0, nums, cache)


def greedy_algorithm_solution(nums):
    current_right_most = len(nums) - 1
    for pos in range(len(nums) - 2, -1, -1):
        if pos + num[pos] >= current_right_most:
            current_right_most = pos

    return current_right_most == 0
