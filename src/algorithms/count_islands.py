def count_islands(mmap):
    max = 0
    for row, row_elem in enumerate(mmap):
        for col, col_elem in enumerate(row_elem):
            if col_elem == "L":
                size = 1
                row_elem[col] = "O"
                size = get_island_size(mmap, row, col, size)
                if size > max:
                    max = size
    return max

def get_island_size(mmap, row, col, initial_size):
    total_size = initial_size

    # check west
    if col - 1 == -1:
        print("Not on real west. Out of bounds")
    elif mmap[row][col - 1] == "L":
        mmap[row][col - 1] = "O"
        total_size = total_size + 1
        total_size = get_island_size(mmap, row, col - 1, total_size)
    
    # check north
    if row - 1 == -1:
        print("Not on real north. Out of bounds.")     
    elif mmap[row - 1][col] == "L":
        mmap[row - 1][col] = "O"
        total_size = total_size + 1
        total_size = get_island_size(mmap, row - 1, col, total_size)

    # check east
    if col + 1 > len(mmap[row]) - 1:
        print("Not on real east. Out of bounds")
    elif mmap[row][col + 1] == "L":
        mmap[row][col + 1] = "O"
        total_size = total_size + 1
        total_size = get_island_size(mmap, row, col + 1, total_size)

    # check south
    if row + 1 > len(mmap) - 1:
        print("Not on real south. Out of bounds.")  
    elif mmap[row + 1][col] == "L":
        mmap[row + 1][col] = "O"
        total_size = total_size + 1
        total_size = get_island_size(mmap, row + 1, col, total_size)

    return total_size