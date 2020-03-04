# battleship game v2
# Solution using class; does not manage a board
class BattleshipGame:
    def __init__(self, ships):
        """A class representing a Battleship Game that we played as kids.
            Args:
                ships (list): a list of dictionaries in which the key-value pair
                is a ship name to a set of the positions of every spot of the ship.
                An example: >>> [ {"submarine":
                                        {(0,0), (0,1), (0,2) }
                                    },
                                  {"carrier":
                                        { (10,0), (10,1), (10,2), (10,3) }
                                    },
                                ]

        """
        self.ships = ships

    def fire_missile(self, target):
        """Given a target, a simple (x,y) coordinate, return one of four responses: miss, hit, sunk, win

            :param target: The x,y coordinates of a target that the missile is fired into
            :type target: tuple
            :returns: str -- One of four responses: miss, hit, sunk, win
        """
        for ship_index, ship in enumerate(self.ships):
            for ship_name, posn in ship.items():
                if target in posn:
                    posn.discard(target)
                    if len(posn) == 0:
                        self.ships.pop(ship_index)
                        if len(self.ships) == 0:
                            return "win"
                        return "sunk"
                    else:
                        ship.update({ship_name: posn})
                        return "hit"
        return "miss"


# battleship game v1
# solution using functions
def setup_battlefield(ships):
    battlefield = [[None] * 10 for _ in range(10)]

    for index, ship in enumerate(ships):
        bow_posn = ship[0]
        head_posn = ship[1]
        ship_number = f"S{index + 1}"

        if bow_posn == head_posn:
            battlefield[bow_posn[0]][bow_posn[1]] = ship_number

        elif bow_posn[0] == head_posn[0]:  # horizontal ship
            length_ship = head_posn[1] - bow_posn[1] + 1
            row = bow_posn[0]
            start = bow_posn[1] - 1
            for _ in range(length_ship):
                start += 1
                battlefield[row][start] = ship_number

        elif bow_posn[1] == head_posn[1]:  # vertical ship
            length_ship = head_posn[0] - bow_posn[0] + 1
            col = bow_posn[1]
            start = bow_posn[0] - 1
            for _ in range(length_ship):
                start += 1
                battlefield[start][col] = ship_number

    return battlefield


def fire_missile(row, col, **kwargs):
    battlefield = kwargs.get("battlefield", None)
    return fire_missle_naive_solution(battlefield, row, col)
    # return fire_missle_recursive_solution(battlefield, row, col)


def fire_missle_naive_solution(battlefield, row, col):
    ship = battlefield[row][col]
    battlefield[row][col] = None
    if ship:
        for _, row_elem in enumerate(battlefield):
            for _, col_elem in enumerate(row_elem):
                if col_elem == ship:
                    return "Hit"
        return "Sink"
    return "Miss"


# TODO: fix bug in dfs
def fire_missle_recursive_solution(battlefield, row, col):
    spot = battlefield[row][col]

    if not spot:
        return "Miss"

    # only do this for the original coordinates
    if spot[len(spot) - 1] != "H":
        spot_hit = spot + "H"
        # battlefield[row][col] = spot_hit
    else:
        spot_hit = spot
        spot = spot[:-1]

    # check up
    if row - 1 >= 0 and battlefield[row - 1][col] == spot:
        return "Hit"
    elif row - 1 >= 0 and battlefield[row - 1][col] == spot_hit:
        fire_missle_recursive_solution(battlefield, row - 1, col)

    # check down
    elif row + 1 < len(battlefield) and battlefield[row + 1][col] == spot:
        return "Hit"
    elif row + 1 < len(battlefield) and battlefield[row + 1][col] == spot_hit:
        fire_missle_recursive_solution(battlefield, row + 1, col)

    # check left
    elif col - 1 >= 0 and battlefield[row][col - 1] == spot:
        return "Hit"
    elif col - 1 >= 0 and battlefield[row][col - 1] == spot_hit:
        return fire_missle_recursive_solution(battlefield, row, col - 1)

    # check right
    elif col + 1 < len(battlefield[row]) and battlefield[row][col + 1] == spot:
        return "Hit"
    elif col + 1 < len(battlefield[row]) and battlefield[row][col + 1] == spot_hit:
        fire_missle_recursive_solution(battlefield, row, col + 1)

    return "Sink"
