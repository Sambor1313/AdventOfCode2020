import sys
import numpy as np
from utils import records_getter, lvl_runner


def kernel(arr, pos):
    occupied = 0
    if arr[pos[0]-1][pos[1]-1] == "#":
        occupied += 1
    if arr[pos[0]][pos[1]-1] == "#":
        occupied += 1
    if arr[pos[0]+1][pos[1]-1] == "#":
        occupied += 1
    if arr[pos[0]-1][pos[1]] == "#":
        occupied += 1
    if arr[pos[0]+1][pos[1]] == "#":
        occupied += 1
    if arr[pos[0]-1][pos[1]+1] == "#":
        occupied += 1
    if arr[pos[0]][pos[1]+1] == "#":
        occupied += 1
    if arr[pos[0]+1][pos[1]+1] == "#":
        occupied += 1
    return occupied


def lvl_first():
    seats = records_getter("d11_seating.txt")
    seats = [list(row) for row in seats]
    seats = np.array(seats)
    seats_padded = np.pad(seats, (1, 1), constant_values='.')

    col_number = len(seats_padded[0])
    row_number = len(seats_padded)
    unique, counts = np.unique(seats_padded, return_counts=True)
    dict_coup_count = dict(zip(unique, counts))
    # print("Empty space:", dict_coup_count['.'],
    #       ", seats:", dict_coup_count['L'])
    previous_seats = seats_padded.copy()
    stabilized = False

    while not stabilized:
        stabilized = True
        for row in range(1, row_number-1):
            for col in range(1, col_number-1):
                if previous_seats[row][col] == "L":
                    if kernel(previous_seats, (row, col)) == 0:
                        seats_padded[row][col] = "#"
                        stabilized = False
                elif previous_seats[row][col] == "#":
                    if kernel(previous_seats, (row, col)) >= 4:
                        seats_padded[row][col] = "L"
                        stabilized = False
        previous_seats = seats_padded.copy()

    unique, counts = np.unique(seats_padded, return_counts=True)
    dict_coup_count = dict(zip(unique, counts))
    print("Occupied when (4 empty nearby):", dict_coup_count['#'])


def sight_checker(arr, pos):
    directions = [(1, 1), (0, 1), (-1, 1), (-1, 0),
                  (1, 0), (-1, -1), (0, -1), (1, -1)]
    occupied = 0
    for direction in directions:
        horizon = False
        sight_step = pos
        while not horizon:
            sight_step = (sight_step[0] + direction[0],
                          sight_step[1] + direction[1])
            if sight_step[0] < 0 or sight_step[1] < 0 or sight_step[0] >= len(arr) or sight_step[1] >= len(arr[0]):
                horizon = True
            elif arr[sight_step[0]][sight_step[1]] == '.':
                pass
            elif arr[sight_step[0]][sight_step[1]] == 'L':
                horizon = True
            elif arr[sight_step[0]][sight_step[1]] == '#':
                occupied += 1
                horizon = True

    return occupied


def lvl_second():
    seats = records_getter("d11_seating.txt")
    seats = [list(row) for row in seats]
    seats = np.array(seats)
    seats_padded = np.pad(seats, (1, 1), constant_values='.')

    col_number = len(seats_padded[0])
    row_number = len(seats_padded)

    previous_seats = seats_padded.copy()
    stabilized = False
    while not stabilized:
        stabilized = True
        for row in range(1, row_number-1):
            for col in range(1, col_number-1):
                if previous_seats[row][col] == "L":
                    if sight_checker(previous_seats, (row, col)) == 0:
                        seats_padded[row][col] = "#"
                        stabilized = False
                elif previous_seats[row][col] == "#":
                    if sight_checker(previous_seats, (row, col)) >= 5:
                        seats_padded[row][col] = "L"
                        stabilized = False
        previous_seats = seats_padded.copy()

    unique, counts = np.unique(seats_padded, return_counts=True)
    dict_coup_count = dict(zip(unique, counts))
    print("Occupied seats when 5 in sight range:", dict_coup_count['#'])


lvl_runner(sys.argv, lvl_first, lvl_second)
