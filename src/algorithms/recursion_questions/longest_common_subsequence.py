def lcm(text1, text2):
    """
    Given two strings text1 and text2, return the length of their longest common subsequence.

    A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

    If there is no common subsequence, return 0.
    """
    row_length = len(text1) + 1  # height of the dp matrix
    col_length = len(text2) + 1  # width of the dp matrix
    cell = [[0] * col_length for _ in range(row_length)]

    for row_index in range(1, row_length):
        for col_index in range(1, col_length):
            if text1[row_index - 1] == text2[col_index - 1]:
                cell[row_index][col_index] = cell[row_index - 1][col_index - 1] + 1
            else:
                cell[row_index][col_index] = max(
                    cell[row_index][col_index - 1], cell[row_index - 1][col_index]
                )

    return cell[row_length - 1][col_length - 1]
