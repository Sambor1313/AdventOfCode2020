import sys
from utils import records_getter, lvl_runner


def data_aug():
    shuttle = records_getter("d13_shuttle.txt")

    arrival_time = int(shuttle[0])
    lines = [int(i) for i in shuttle[1].split(',') if i != "x"]
    return shuttle, arrival_time, lines


def first_lvl():
    shuttle, arrival_time, lines = data_aug()
    waiting_time = 0
    my_bus = 0
    while not my_bus:
        for line in lines:
            if ((arrival_time + waiting_time) % line) == 0:
                my_bus = line
                break
        waiting_time += 1
    waiting_time -= 1

    print("My bus is", my_bus, "will arrive in", waiting_time)
    print("Result", my_bus * waiting_time)

# Second prg


def second_lvl():
    # Create list of line tuples (ID number, t-offset)
    shuttle, arrival_time, lines = data_aug()
    tlines = [(int(i), idx) if i != "x" else 0 for idx,
              i in enumerate(shuttle[1].split(',')) if i != "x"]
    tlines.sort(key=lambda tup: -tup[0])
    # print(tlines)

    while len(tlines) > 1:
        a = tlines[0]
        b = tlines[1]
        n0 = a[0] * b[0]
        m = 0
        while True:
            if (a[0] * m + a[1] - b[1]) % b[0] == 0:
                n1 = m
                break
            m += 1
        tlines = [(n0, a[1])] + tlines[2:]
        # print(tlines)

    print("Result not optiman, not accepted, t =", tlines[0])


lvl_runner(sys.argv, first_lvl, second_lvl)
