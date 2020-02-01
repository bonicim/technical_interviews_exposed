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

"""Commentary

The naive solution is the check every substring and determine if it is a palindrome and the largest one we have seen so far.
Verification of a palindrome in any string takes n time. Going through every substring take n^2 time. Thus the total runtime is n^3.

The dynamic programming solution uses a two dimensional matrix to keep track of computations, thus improving the naive solution. We can build a bottom
up solution by realizing that we can know the palindrome status for one and two characters. Those are our base cases and will setup our matrix. Having
the palindrome status for one and two characters will allow us to calculate the largest paindromic substring by observing the following recurrence:

    If the substring is_palindrome[left + 1][right - 1] is True and the current substring s[left] == s[right], then that substring s[left:right] is a palindrome
    Otherwise, it's not.

We can also arrive at a different solution by observing that palindromes are symmetrical around the center. Thus a string is a palindrome if
the substrings to the left and right of the center are the same. In fact, we can think of expanding from the center to determine if a string
is a palindrome. Expanding from the center takes n^2 runtime but at a cost of constant space because we can keep track of the pointers of the largest palindrome.
The runtime is n^2 because palindromes can have centers between two letters such as "abba" as opposed to "ava". Thus, we have to expand from the center
for every letter and for every two contiguous letters.
"""


def longest_palindrome(string):
    # return expand_from_middle_solution(string)
    return dynamic_programming_solution(string)
    # return brute_force_solution(string)


def brute_force_solution(string):
    def is_palindrome(string, i, j):
        while i <= j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    max_len = 0
    result = ""

    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string, i, j):
                len_of_current_palindrome = j + 1 - i
                if len_of_current_palindrome > max_len:
                    max_len = len_of_current_palindrome
                    result = string[i : j + 1]

    return result


def expand_from_middle_solution(string):
    def length_palindrome(string, left, right):
        if not string or left > right:
            return 0

        # ensure that the left and right are within bounds
        # the last condition will enforce the palindrome property by breaking out of the while loop and returning the length of the current palindrome
        # in other words it stops expanding the window when the characters don't match
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1

        return right - left - 1

    def start_index(center, length):
        return center - (
            (length - 1) // 2
        )  # we have to subtract 1 from the length because our string array starts at index 0. If we didn't do this, we would go one over the starting position of the palindrome

    def end_index(center, length):
        return center + (length // 2)

    max_len_palindrome_start = 0
    max_len_palindrome_end = 0
    max_len_palindrome = max_len_palindrome_end - max_len_palindrome_start

    for center in range(len(string)):
        len_palindrome_odd_length_substring = length_palindrome(string, center, center)
        len_palindrome_even_length_substring = length_palindrome(
            string, center, center + 1
        )

        current_max_len_palindrome = max(
            len_palindrome_odd_length_substring, len_palindrome_even_length_substring
        )

        if current_max_len_palindrome > max_len_palindrome:
            max_len_palindrome_start = start_index(center, current_max_len_palindrome)
            max_len_palindrome_end = end_index(center, current_max_len_palindrome)
            max_len_palindrome = max_len_palindrome_end - max_len_palindrome_start

    return string[max_len_palindrome_start : max_len_palindrome_end + 1]


def dynamic_programming_solution(string):
    if len(string) == 0:
        return string

    is_palindrome = [[False for _ in range(len(string))] for _ in range(len(string))]
    start = 0
    max_length = 1

    # setup substrings of single characters
    for index in range(len(string)):
        is_palindrome[index][index] = True

    # setup substrings of two characters
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            is_palindrome[index][index + 1] = True
            start = index
            max_length = 2

    # for substrings of length three or greater, we check if all the inner substrings are also palindromes.
    # if all the inner substrings are palindromes, then the current length is also a palindrome
    for substring_length in range(
        3, len(string) + 1
    ):  # we add one to the length of the string because we want to explore the substring at the last index; this is a unique to the range function, it excludes the provided stopping point
        end_index = len(string) - substring_length + 1
        # this is where we check all the inner substrings
        for left_index in range(end_index):
            right_index = left_index + substring_length - 1

            # this is where we check the current inner substring
            # it checks the cell block that is down and to the left in the matrix
            # that spot is the palindrome status of the current substring
            is_substring_a_palindrome = is_palindrome[left_index + 1][right_index - 1]

            # since we are checking palindromes from left to right, we update the cache and the length and start index of the current palindrome
            # in other words, our palindrome answer accumulates as we expand our palindrome to three or greater characters
            if is_substring_a_palindrome and string[left_index] == string[right_index]:
                is_palindrome[left_index][right_index] = True
                max_length = substring_length
                start = left_index

    return string[start : start + max_length]
