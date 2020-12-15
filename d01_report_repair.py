import sys
from utils import records_getter, lvl_runner


def second_lvl():
    strings = records_getter("d1_elves.txt")
    digits = [int(i) for i in strings]

    for idx, digit in enumerate(digits):
        for idxx, d in enumerate(digits[idx+1:]):
            for dd in digits[idxx+2:]:
                if digit + d + dd == 2020:
                    print(digit * d * dd)
                    break


lvl_runner(sys.argv, None, second_lvl)
