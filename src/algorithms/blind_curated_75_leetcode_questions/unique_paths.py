""" Commentary
This problem tests your command of searching algorithms and dynamic programming, both
of which can solve this question.

One strategy is to step through a simple example if you're stuck and don't know where to start.

The dynamic programming solution is quite easy to grasp. The best way to do that is to draw a picture of the search space. Then given the constraints of the problem,
update the number of total paths to each box. In this case, the top and left rows should all have a value
of 1 because there is only one way to that box given the constraints of the problem.

After that, we notice that we can the determine the number of ways to each box by looking at the number of
ways to get to that box's previous boxes or neighbors. We keep going through the whole matrix until we reach
the target. At that point, we will have arrived at the answer which was built on the answers of previous smaller problems.
"""


def uniquePaths(m, n):
    # create a visual representation of the board as a matrix
    ways_to_cell = [[0] * m for _ in range(n)]

    # Given that we can only travel south and east, we know that there is only way to reach
    # the destinations on the northern and western border of the board
    # for index, _ in enumerate(ways_to_cell[0]):
    #     ways_to_cell[0][index] = 1
    for row_index in range(len(ways_to_cell[0])):
        ways_to_cell[0][row_index] = 1

    for _, row_elem in enumerate(ways_to_cell):
        row_elem[0] = 1

    # Explore every inner destination and update the num of paths for each destination
    # the number of paths is each destination is the num of paths to the each of its neighbors, i.e. the left and upper neighbors
    for row_index in range(1, len(ways_to_cell)):
        for col_index in range(1, len(ways_to_cell[row_index])):
            ways_to_cell[row_index][col_index] = (
                ways_to_cell[row_index - 1][col_index]
                + ways_to_cell[row_index][col_index - 1]
            )

    return ways_to_cell[n - 1][m - 1]
