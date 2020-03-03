def memory_heavy_solution(matrix):
    rows = [False] * len(matrix)  # height
    cols = [False] * len(matrix[0])  # width

    for row, row_elem in enumerate(matrix):
        for col, col_elem in enumerate(row_elem):
            if col_elem == 0:
                cols[col] = True
                rows[row] = True

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if rows[row] or cols[col]:
                matrix[row][col] = 0


def memory_width_only_solution(matrix):
    cols = [False] * len(matrix[0])  # width

    for row, row_elem in enumerate(matrix):
        for col, col_elem in enumerate(row_elem):
            if col_elem == 0:
                cols[col] = True

    for row in range(len(matrix)):
        contains_zero = False
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                contains_zero = True
                break
        for col in range(len(matrix[row])):
            if contains_zero or cols[col]:
                matrix[row][col] = 0


def constant_memory_solution(matrix):
    first_row_zero = False
    for _, col_elem in enumerate(matrix[0]):
        if col_elem == 0:
            first_row_zero = True
            break

    # set the first row to zero if column below has a zero
    for _, row_elem in enumerate(matrix):
        for col, col_elem in enumerate(row_elem):
            if col_elem == 0:
                matrix[0][
                    col
                ] = 0  # whole column is zero, so set the first row at col to zero

    for row in range(1, len(matrix)):
        row_contains_zero = False
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                row_contains_zero = True
                break
        for col in range(len(matrix[row])):
            if row_contains_zero or matrix[0][col] == 0:
                matrix[row][col] = 0

    if first_row_zero:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0
