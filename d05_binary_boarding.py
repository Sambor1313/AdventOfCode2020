import sys
from utils import records_getter, lvl_runner


def boarding():
    seat_keys = records_getter('d5_airplane.txt')

    highest_seat = 0
    not_mine_seat = []

    for seat_key in seat_keys:
        start = 0
        end = 127
        row = 0

        # Row seeker
        for d in seat_key[:7]:
            if d == 'F':
                end = int((start + end)/2)
            elif d == 'B':
                start = int((start + end + 1)/2)
            else:
                break
        if start == end:
            row = start
        else:
            print("Err on row:", seat_key)

        # Col seeker
        start = 0
        end = 7
        col = 0
        for d in seat_key[7:]:
            if d == 'L':
                end = int((start + end)/2)
            elif d == 'R':
                start = int((start + end + 1)/2)
            else:
                break
        if start == end:
            col = start
        else:
            print("Err on col:", seat_key)

        not_mine_seat.append(8 * row + col)

        if highest_seat < 8 * row + col:
            highest_seat = 8 * row + col

        #print("Seat_key:", seat_key, ": Row:", row, ", Col:", col)
    return highest_seat, not_mine_seat


def which_is_mine(not_mine_seat):
    not_mine_seat.sort()
    for idx, s in enumerate(not_mine_seat):
        if not (not_mine_seat[idx] + 1) == not_mine_seat[idx+1]:
            your_seat = not_mine_seat[idx+1]
            break
    print("Your seat:", your_seat)


def lvl_first():
    highest_seat, _ = boarding()
    print("Highest seat:", highest_seat)


def lvl_second():
    highest_seat, not_mine = boarding()
    which_is_mine(not_mine)


lvl_runner(sys.argv, lvl_first, lvl_second)
