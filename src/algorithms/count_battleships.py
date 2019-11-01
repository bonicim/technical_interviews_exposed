def count_battleships(ocean_map):
    # return count_battleships_recursive_solution(ocean_map)
    return count_battleships_non_recursive_solution(ocean_map)


def count_battleships_recursive_solution(ocean_map):
    def sink_ship(row, col):
        ocean_map[row][col] = "."

        if row - 1 != -1 and ocean_map[row - 1][col] == "X":
            sink_ship(row - 1, col)

        if row + 1 < len(ocean_map) and ocean_map[row + 1][col] == "X":
            sink_ship(row + 1, col)

        if col - 1 != -1 and ocean_map[row][col - 1] == "X":
            sink_ship(row, col - 1)

        if col + 1 < len(ocean_map[row]) and ocean_map[row][col + 1] == "X":
            sink_ship(row, col + 1)

    ship_count = 0
    for row, row_elem in enumerate(ocean_map):
        for col, col_elem in enumerate(row_elem):
            if col_elem == "X":
                ship_count = ship_count + 1
                sink_ship(row, col)

    return ship_count


# Does not change the map or use recursion
def count_battleships_non_recursive_solution(ocean_map):
    ship_count = 0
    for row, row_elem in enumerate(ocean_map):
        for col, col_elem in enumerate(row_elem):
            if col_elem == ".":
                continue
            if row - 1 >= 0 and ocean_map[row - 1][col] == "X":
                continue
            if col - 1 >= 0 and ocean_map[row][col - 1] == "X":
                continue
            ship_count += 1

    return ship_count
