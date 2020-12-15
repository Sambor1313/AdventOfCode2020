import sys
from utils import records_getter, lvl_runner


rows = records_getter("d3_forest.txt")

pattern_len = rows[0].__len__()


def slop_counter(right, down=1):
    f = 0
    encounter = 0

    for row in rows[::down]:
        if row[f % pattern_len] == '#':
            encounter += 1
        f += right
    return encounter


def first_slop():
    print(f"Tobbogan encounter {slop_counter(3)} trees")


def couple_slides():
    traverses = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

    mult = 1
    for travers in traverses:
        mult *= slop_counter(*travers)

    print("Multiplication of slides:", mult)


lvl_runner(sys.argv, first_slop, couple_slides)
