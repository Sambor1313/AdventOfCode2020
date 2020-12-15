import sys
from utils import records_getter, lvl_runner


def first_combination():
    jolts_levels = records_getter("d10_adaptedarray.txt")

    sorted_jolts = [int(i) for i in jolts_levels]
    sorted_jolts.sort()
    # Adding my device
    sorted_jolts.append(sorted_jolts[-1]+3)

    previous_joltage = 0
    adapters = [0, 0, 0]

    for jolt in sorted_jolts:
        adapters[jolt - previous_joltage - 1] += 1
        previous_joltage = jolt

    print("Voltage 1:", adapters[0], "| Voltage 2:",
          adapters[1], "| Voltage 3:", adapters[2])
    print("Mulitiplication:", adapters[0] * adapters[2])


def all_combinations():
    jolts_levels = records_getter("d10_adaptedarray.txt")

    sorted_jolts = [int(i) for i in jolts_levels]
    sorted_jolts.sort()
    # Adding my device
    sorted_jolts.append(sorted_jolts[-1]+3)
    previous_joltage = 0
    branches = 1
    ones_handler = 0
    for jolt in sorted_jolts:
        if jolt - previous_joltage == 1:
            ones_handler += 1
        elif jolt - previous_joltage == 3:
            if ones_handler == 0:
                branches *= 1
            elif ones_handler == 1:
                branches *= 1
            elif ones_handler == 2:
                branches *= 2
            elif ones_handler == 3:
                branches *= 4
            elif ones_handler == 4:
                branches *= 7
            else:
                branches *= 0
            ones_handler = 0
        else:
            print("Error")
        previous_joltage = jolt
    print("Ways to connect:", branches)


lvl_runner(sys.argv, first_combination, all_combinations)
