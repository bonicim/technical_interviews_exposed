def longest_palindrome(string):
    """
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example 1:

    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
    Example 2:

    Input: "cbbd"
    Output: "bb"
    """

    # return expand_from_middle_solution(string)
    return dynamic_programming_solution(string)


def expand_from_middle_solution(string):
    def largest_palindrome_len(string, left, right):
        if not string or left > right:
            return 0

        # ensure that the left and right are within bounds
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return right - left - 1

    start = 0
    end = 0

    for index in range(len(string)):
        substring_start_at_center = largest_palindrome_len(string, index, index)
        substring_start_left_right_of_center = largest_palindrome_len(
            string, index, index + 1
        )

        length_palidrome_at_index = max(
            substring_start_at_center, substring_start_left_right_of_center
        )

        if length_palidrome_at_index > (end - start):
            start = index - ((length_palidrome_at_index - 1) // 2)
            end = index + (length_palidrome_at_index // 2)

    return string[start : end + 1]


def dynamic_programming_solution(string):
    if len(string) == 0:
        return string

    cache = [[False for _ in range(len(string))] for _ in range(len(string))]
    start = 0
    max_length = 1

    for index in range(len(string)):
        cache[index][index] = True

    for index in range(len(string) - 1):
        if index < len(string) - 1 and string[index] == string[index + 1]:
            cache[index][index + 1] = True
            start = index
            max_length = 2

    for substring_length in range(3, len(string) + 1):
        final_ending_index = len(string) - substring_length + 1
        for left_index in range(final_ending_index):
            right_index = left_index + substring_length - 1
            is_before_substring_palindrome = cache[left_index + 1][
                right_index - 1
            ]  # inside substring

            if (
                is_before_substring_palindrome
                and string[left_index] == string[right_index]  # outer substring
            ):
                cache[left_index][right_index] = True

                max_length = substring_length
                start = left_index

    return string[start : start + max_length]
