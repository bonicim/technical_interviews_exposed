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
        odd_length_substring = largest_palindrome_len(string, index, index)
        even_length_substring = largest_palindrome_len(string, index, index + 1)

        length_palidrome_at_index = max(odd_length_substring, even_length_substring)

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

    for letters_to_consider in range(3, len(string) + 1):
        largest_index_within_bounds_of_letters_to_consider = (
            len(string) - letters_to_consider + 1
        )
        for left_index in range(largest_index_within_bounds_of_letters_to_consider):
            right_index = left_index + letters_to_consider - 1
            is_before_substring_palindrome = cache[left_index + 1][right_index - 1]

            if (
                is_before_substring_palindrome
                and string[left_index] == string[right_index]
            ):
                cache[left_index][right_index] = True

                max_length = letters_to_consider
                start = left_index

    return string[start : start + max_length]
