import sys
from utils import records_getter, lvl_runner

FACE = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}


def first_lvl():
    orders = records_getter('d12_rain_risk.txt')
    face = 1
    # 1st - N/S (+/-)
    # 2st - E/W (+/-)
    position = (0, 0)

    for order in orders:
        command = order[0]
        value = int(order[1:])

        if command == "N":
            position = (position[0] + value, position[1])
        elif command == "S":
            position = (position[0] - value, position[1])
        elif command == "E":
            position = (position[0], position[1] + value)
        elif command == "W":
            position = (position[0], position[1] - value)
        elif command == "R":
            value /= 90
            face = (face + value) % 4
        elif command == "L":
            value /= 90
            face = (face - value + 4) % 4
        elif command == "F":
            if face == 0:
                position = (position[0] + value, position[1])
            elif face == 2:
                position = (position[0] - value, position[1])
            elif face == 1:
                position = (position[0], position[1] + value)
            elif face == 3:
                position = (position[0], position[1] - value)

    print("Final coordinate:", print_coordinate(*position))
    print("Manhatan distance:", abs(position[0]) + abs(position[1]))


'''
Second part
'''


def second_lvl():
    orders = records_getter('d12_rain_risk.txt')
    face = 1
    # 1st - N/S (+/-)
    # 2st - E/W (+/-)
    position = (0, 0)
    # Waypoint relative to ship
    waypoint = (1, 10)

    for order in orders:
        command = order[0]
        value = int(order[1:])

        if command == "N":
            waypoint = (waypoint[0] + value, waypoint[1])
        elif command == "S":
            waypoint = (waypoint[0] - value, waypoint[1])
        elif command == "E":
            waypoint = (waypoint[0], waypoint[1] + value)
        elif command == "W":
            waypoint = (waypoint[0], waypoint[1] - value)
        elif command == "R":
            for step in range(0, int(value/90)):
                waypoint = (-waypoint[1], waypoint[0])
        elif command == "L":
            for step in range(0, int(value/90)):
                waypoint = (waypoint[1], -waypoint[0])
        elif command == "F":
            position = (position[0] + waypoint[0] * value,
                        position[1] + waypoint[1] * value)

    print("Final coordinate:", print_coordinate(*position))
    print("Manhatan distance:", abs(position[0]) + abs(position[1]))


def print_coordinate(long, lat):
    lo = "N" if long >= 0 else "S"
    la = "E" if lat >= 0 else "W"
    return f"{abs(long)}{lo} {abs(lat)}{la}"


lvl_runner(sys.argv, first_lvl, second_lvl)
