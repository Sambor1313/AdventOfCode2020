import sys
import re
from utils import records_getter, lvl_runner


def cmd_getter():
    commands = records_getter("d14_docking_data.txt")
    # Cmd is list of command tuples (mem adres/-1 if mask, value/mask)
    # Data recognition
    cmd = []
    for command in commands:
        if command[0:3] == 'mas':
            cmd.append((-1, command.split(" = ")[1]))
        else:
            # create a mask instruction
            cmd_temp = re.findall(r"^\w+\[(\d+)\]\D*(\d+)", command)
            cmd.append(cmd_temp[0])
    return cmd

# Program execute


def first_lvl():
    cmd = cmd_getter()
    actual_mask = ""
    memory = {}
    for c in cmd:
        if c[0] == -1:
            actual_mask = c[1]
        else:
            b_value = "{:0>36b}".format(int(c[1]))
            result = "".join([b_value[idx] if m == "X" else m for idx,
                              m in enumerate(actual_mask)])
            memory[c[0]] = result
            # print(b_value)
            # print(actual_mask)
            # print(result)

    print("Sum of the whole memory:", sum(
        [int(i, 2) for i in memory.values()]))

# Program v2


def second_lvl():
    cmd = cmd_getter()
    memory_v2 = {}
    for c in cmd:
        if c[0] == - 1:
            actual_mask = c[1]
        else:
            mem_v = "{:0>36b}".format(int(c[0]))
            mask_temp = "".join([mem_v[idx] if m == "0" else m for idx,
                                 m in enumerate(actual_mask)])
            combination = 2**mask_temp.count('X')
            for i in range(combination):
                mm = ""
                i_fix = ("{:0>"+str(mask_temp.count('X'))+"b}").format(int(i))
                character_no = 0
                for im in mask_temp:
                    if im == "X":
                        mm += i_fix[character_no]
                        character_no += 1
                    else:
                        mm += im
                memory_v2[mm] = c[1]

    print("Suma of the whole memory with floating points:",
          sum([int(i) for i in memory_v2.values()]))


lvl_runner(sys.argv, first_lvl, second_lvl)
