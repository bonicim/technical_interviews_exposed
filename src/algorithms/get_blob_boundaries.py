# Given a matrix, print out the boundaries of a blob and return a dictionary of the boundaries (see tests for examples)
# Blob is defined as having one or more adjacent cell to the top, left, bottom, or right
# A Cell Read is defined as visiting a cell
# Assumptions:
# There can only be exactly one Blob in the 2D array
# There can not be any other blobs or one-cell blobs present
# A blob can have a minimum of two cells or a maximum of the entire array


def get_blob_boundaries(inputGrid):
    counter = {"Cell Reads": 0, "Top": -1, "Left": -1, "Bottom": -1, "Right": -1}
    visited = [[False for _ in range(len(inputGrid[0]))] for _ in range(len(inputGrid))]

    for row_index, row in enumerate(inputGrid):
        for col_index, _ in enumerate(row):
            if not visited[row_index][col_index]:
                visited[row_index][col_index] = True
                counter["Cell Reads"] += 1
                if inputGrid[row_index][col_index]:
                    if counter["Top"] == -1:
                        counter.update({"Top": row_index})
                    if counter["Left"] == -1:
                        counter.update({"Left": col_index})
                    if counter["Bottom"] == -1:
                        counter.update({"Bottom": row_index})
                    if counter["Right"] == -1:
                        counter.update({"Right": col_index})
                    counter, visited = search_blob(
                        inputGrid, row_index, col_index, counter, visited
                    )
                    break

    print(
        f"Cell Reads: {counter['Cell Reads']}\nTop: {counter['Top']}\nLeft: {counter['Left']}\nBottom: {counter['Bottom']}\nRight: {counter['Right']}"
    )
    del counter["Cell Reads"]
    return counter


def search_blob(inputGrid, row_index, col_index, counter, visited):
    # for each conditional, the first conditional checks if the cell is out of bounds and the second conditional checks if the cell has not been visited

    # check top
    if row_index - 1 != -1 and not visited[row_index - 1][col_index]:
        visited[row_index - 1][col_index] = True
        counter["Cell Reads"] += 1
        if inputGrid[row_index - 1][col_index]:
            counter, visited = search_blob(
                inputGrid, row_index - 1, col_index, counter, visited
            )

    # check left
    if col_index - 1 != -1 and not visited[row_index][col_index - 1]:
        visited[row_index][col_index - 1] = True
        counter["Cell Reads"] += 1
        if inputGrid[row_index][col_index - 1]:
            if col_index - 1 < counter["Left"]:
                counter.update({"Left": col_index - 1})
            counter, visited = search_blob(
                inputGrid, row_index, col_index - 1, counter, visited
            )

    # check bottom
    if row_index + 1 <= len(inputGrid) - 1 and not visited[row_index + 1][col_index]:
        visited[row_index + 1][col_index] = True
        counter["Cell Reads"] += 1
        if inputGrid[row_index + 1][col_index]:
            if counter["Bottom"] < row_index + 1:
                counter.update({"Bottom": row_index + 1})
            counter, visited = search_blob(
                inputGrid, row_index + 1, col_index, counter, visited
            )

    # check right
    if (
        col_index + 1 <= len(inputGrid[row_index]) - 1
        and not visited[row_index][col_index + 1]
    ):
        visited[row_index][col_index + 1] = True
        counter["Cell Reads"] += 1
        if inputGrid[row_index][col_index + 1]:
            if counter["Right"] < col_index + 1:
                counter.update({"Right": col_index + 1})
            counter, visited = search_blob(
                inputGrid, row_index, col_index + 1, counter, visited
            )

    return counter, visited
