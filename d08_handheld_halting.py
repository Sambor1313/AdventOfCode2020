import sys
from utils import records_getter, lvl_runner

# First star


def prg_runner(fix_step=-1):
    commands = records_getter("d8_gameboy.txt")
    line = 0
    acc = 0
    executed_line_iter = 0
    while not commands[line] == "ed":
        cmd = commands[line][:3]
        line_save = line
        if executed_line_iter == fix_step:
            if cmd == "nop":
                cmd = "jmp"
            elif cmd == "jmp":
                cmd = "nop"

        if cmd == "nop":
            line += 1
        elif cmd == "acc":
            if commands[line][4] == "+":
                m = 1
            else:
                m = -1
            acc += m * int(commands[line][5:])
            line += 1
        elif cmd == "jmp":
            if commands[line][4] == "+":
                m = 1
            else:
                m = -1
            line += m * int(commands[line][5:])
        commands[line_save] = "ed"
        if line == len(commands):
            return True, acc
        executed_line_iter += 1
    return False, acc


def fixing_loop():
    commands = records_getter("d8_gameboy.txt")
    save_commands = commands.copy()
    fixing_set = 0
    terminate = False
    acc = 0
    # Second star
    while not terminate:
        terminate, acc = prg_runner(fixing_set)
        # Reset and next command fixing
        commands = save_commands.copy()
        fixing_set += 1
    print("An accumultor-fixed value: ", acc)


def test_prg():
    print("An accumulator value, after execute: ", prg_runner()[1])


lvl_runner(sys.argv, test_prg, fixing_loop)
