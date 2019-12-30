def count_palindromic_substrings(string):
    """
    Given a string, your task is to count how many palindromic substrings in this string.

    The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

    Example 1:

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".


    Example 2:

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
    """
    # return expand_from_center_solution(string)
    return dynamic_programming_solution(string)


# This solution is n^2 runtime
def expand_from_center_solution(string):
    def count_all_palindromic_substrings(left, right, string):
        count = 0

        while left >= 0 and right < len(string) and string[left] == string[right]:
            count += 1
            left -= 1
            right += 1

        return count

    total_count = 0

    for index in range(len(string)):
        count_substrings_from_center = count_all_palindromic_substrings(
            index, index, string
        )
        count_substrings_from_left_right_of_center = count_all_palindromic_substrings(
            index, index + 1, string
        )
        total_count = (
            total_count
            + count_substrings_from_center
            + count_substrings_from_left_right_of_center
        )

    return total_count


def dynamic_programming_solution(string):
    if len(string) == 0:
        return 0

    cache = [[False for _ in range(len(string))] for _ in range(len(string))]
    total_count = 0

    for index in range(len(string)):
        cache[index][index] = True
        total_count += 1

    for index in range(len(string) - 1):
        if index < len(string) - 1 and string[index] == string[index + 1]:
            cache[index][index + 1] = True
            total_count += 1

    for length_substring in range(3, len(string) + 1):
        final_ending_index = len(string) - length_substring + 1

        for start_index in range(final_ending_index):
            local_ending_index = start_index + length_substring - 1
            has_inner_palindromic_substring = cache[start_index + 1][
                local_ending_index - 1
            ]
            has_outer_palindromic_substring = (
                string[start_index] == string[local_ending_index]
            )

            if has_inner_palindromic_substring and has_outer_palindromic_substring:
                cache[start_index][local_ending_index] = True
                total_count += 1

    return total_count
