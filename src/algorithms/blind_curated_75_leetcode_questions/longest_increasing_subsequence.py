def longest_increasing_subsequence(nums):
    """
    Given an unsorted array of integers, find the length of longest increasing subsequence.

    Example:

    Input: [10,9,2,5,3,7,101,18]
    Output: 4
    Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    """
    return dynamic_programming_solution(nums)


def dynamic_programming_solution(nums):
    longest_subsequence = [1] * len(nums)
    max_longest_subsequence = 0

    for curr_index, curr_num in enumerate(nums):
        for prev_index in range(curr_index):
            prev_num = nums[prev_index]

            if curr_num > prev_num:
                prev_num_longest_subsequence = longest_subsequence[prev_index]
                curr_num_longest_subsequence = longest_subsequence[curr_index]

                longest_subsequence[curr_index] = max(
                    curr_num_longest_subsequence, 1 + prev_num_longest_subsequence
                )
        max_longest_subsequence = max(
            max_longest_subsequence, longest_subsequence[curr_index]
        )

    return max_longest_subsequence
