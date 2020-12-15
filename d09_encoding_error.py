import sys
from utils import records_getter, lvl_runner


def first_lvl():
    numbers = records_getter("d9_XMAS.txt")
    window = 25
    for idx, number in enumerate(numbers[window:]):
        checker = False
        for a in numbers[idx:idx+window-1]:
            for b in numbers[idx+1:idx+window]:
                if (int(a) + int(b) == int(number)):
                    checker = True
        if not checker:
            invalid_no = int(number)
            break
    return invalid_no


def second_lvl():
    numbers = records_getter("d9_XMAS.txt")
    invalid_no = first_lvl()
    for window in range(2, 40):
        for idx in range(0, len(numbers)-window):
            handler = [int(i) for i in numbers[idx:idx+window]]
            suma = sum(handler)
            if suma == invalid_no:
                print("Biggest + smallest numbers: ",
                      max(handler)+min(handler))


def first_lvl_runner():
    print("First number without property:", first_lvl())


lvl_runner(sys.argv, first_lvl_runner, second_lvl)
