"""  9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row
from the field.

Example:

# FIELD

[[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]]

Will return : [(2, 2), (3, 4), (2, 4)] """


def inadequate_seat(seats):
    seat_position = []
    col_and_poz = []
    for col in range(0, len(seats[0])):
        current_col = []
        matr_poz = []
        for line in range(len(seats)-1, -1, -1):
            current_col.append(seats[line][col])
            matr_poz.append([line, col])
        col_and_poz.append((current_col, matr_poz))
    for pair in col_and_poz:
        heights = pair[0]
        poz = pair[1]
        for index1, first_pers in enumerate(heights):
            for index2, second_pers in enumerate(heights[index1+1:]):
                if first_pers <= second_pers:
                    if tuple(poz[index1]) not in seat_position:
                        seat_position.append(tuple(poz[index1]))
    return seat_position


def main():

    seats = [[1, 2, 3, 2, 1, 1],
             [2, 4, 4, 3, 7, 2],
             [5, 5, 2, 5, 6, 4],
             [6, 6, 7, 6, 7, 5]]
    seat_position = inadequate_seat(seats)
    print(seat_position)


if __name__ == "__main__":
    main()
