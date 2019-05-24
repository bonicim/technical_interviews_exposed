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

def get_lowest_integer(int, remove):
    # convert string to int
    # put the int into an array
    # create a stack and put the first digit in it
    #   
    # Step Two: Go through every digit in the int array and push it in
    # the stack, checking if the number being pushed is less than the
    # number on the top of the stack and then popping as needed
    
    # with the leftover stack pop everything into another stack and then pop it again and 
    # convert to a string, which will be the final answer

    return None
