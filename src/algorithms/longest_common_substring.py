def lcs(text1, text2):
    row_length = len(text1) + 1  # height of the dp matrix
    col_length = len(text2) + 1  # width of the dp matrix
    cell = [[0] * col_length for _ in range(row_length)]
    largest_substring_len = 0

    for row_index in range(1, row_length):
        for col_index in range(1, col_length):
            if text1[row_index - 1] == text2[col_index - 1]:
                cell[row_index][col_index] = cell[row_index - 1][col_index - 1] + 1
                if cell[row_index][col_index] > largest_substring_len:
                    largest_substring_len = cell[row_index][col_index]
            else:
                cell[row_index][col_index] = 0

    return largest_substring_len
