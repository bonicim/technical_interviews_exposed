def count_islands(matrix):
    island_count = 0
    for row, rows in enumerate(matrix):
        for col, cols in enumerate(rows):
            if cols == "L":
                island_count += 1
                _remove_island(matrix, row, col)

    return island_count


def _remove_island(matrix, row, col):
    row_boundary = len(matrix) - 1
    col_boundary = len(matrix[0]) - 1

    # base cases
    # outside of the rows
    if row < 0 or row > row_boundary:
        return
    # outside of the columns
    if col < 0 or col > col_boundary:
        return
    # moved from island to a non-island
    if matrix[row][col] == "O":
        return

    matrix[row][col] = "O"
    _remove_island(matrix, row - 1, col)
    _remove_island(matrix, row + 1, col)
    _remove_island(matrix, row, col + 1)
    _remove_island(matrix, row, col - 1)


# provided method for getting the size of an island
# handles the case where the matrix can have rows or columns or varying heights
def get_island_size(matrix, row, col, initial_size):
    total_size = initial_size

    # check west
    if col - 1 == -1:
        print("Not on real west. Out of bounds")
    elif matrix[row][col - 1] == "L":
        matrix[row][col - 1] = "O"
        total_size = total_size + 1
        total_size = get_island_size(matrix, row, col - 1, total_size)

    # check north
    if row - 1 == -1:
        print("Not on real north. Out of bounds.")
    elif matrix[row - 1][col] == "L":
        matrix[row - 1][col] = "O"
        total_size = total_size + 1
        total_size = get_island_size(matrix, row - 1, col, total_size)

    # check east
    if col + 1 > len(matrix[row]) - 1:
        print("Not on real east. Out of bounds")
    elif matrix[row][col + 1] == "L":
        matrix[row][col + 1] = "O"
        total_size = total_size + 1
        total_size = get_island_size(matrix, row, col + 1, total_size)

    # check south
    if row + 1 > len(matrix) - 1:
        print("Not on real south. Out of bounds.")
    elif matrix[row + 1][col] == "L":
        matrix[row + 1][col] = "O"
        total_size = total_size + 1
        total_size = get_island_size(matrix, row + 1, col, total_size)

    return total_size
