"""
An airplane divides its row seating into three sections: left, middle, and right.
It has the following configuration for its seats:

Row: ABC DEFG HJK

Each section is separated by an aisle. 

Your task is to find the total number of available groups of three, in which each seat is adjacent 
and is touching each other. For example, if there are no seats reserved for a given row, then there
are 3 available groups of three. 

In another example, if there is only one row and seat 1E is reserved, then only 2 groups of three are available.

Note that if a seat is separated from an aisle, it is not considered adjacent. Thus, if seats
1B, 1C, and 1D were available, that does NOT constitute a group of three. They must be touching each other. 

Given a string that represents all reserved seats and the number of rows on an airplane, return the 
total number of available groups of three. 

Examples:

("1A", 3) => 8 
("", 1) => 3
("2D 2E", 2) => 5 

"""

def count_available_seats(reservations, rows):
    # This is a quick and dirty solution simply to show one way of solving this problem

    reserved = reservations.split()
    seats = 10
    seating_chart = [[False for _ in range(seats)] for _ in range(rows + 1)]
    ascii_count = 65
    # translating seat letters to numbers to be used for accessing the seating chart
    seat_to_index = {chr(ascii_count + n): n  for n in range(seats)}
    seat_to_index.update({'J':8})
    seat_to_index.pop('I')
    seat_to_index.update({'K':9})

    # update seating chart with reserved seats
    for seat in reserved:
        row = int(seat[0])
        seat_letter_index = seat_to_index[seat[1]]
        seating_chart[row][seat_letter_index] = True

    groups_of_3 = 0
    for row in range(1, rows + 1):
        groups_of_3 += get_open_groups_of_3(seating_chart[row])
    
    return groups_of_3

def get_open_groups_of_3(row_chart):
    count = 3
    # check seats A,B,C
    for val in range(0, 3):
        if row_chart[val]:
            count -= 1
            break
    # check seats H,J,K
    for val in range(7, 10):
        if row_chart[val]:
            count -= 1
            break
    # check seats D,E,F,G     
    if row_chart[3] and row_chart[6]:
        count -= 1
    elif row_chart[4] or row_chart[5]:
        count -= 1

    return count