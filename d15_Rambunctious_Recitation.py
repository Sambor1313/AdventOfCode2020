import sys
from utils import lvl_runner

input = [0, 13, 1, 16, 6, 17]
test_one = [2, 1, 3]


def big_o_square():
    first_eg = input.copy()
    for i in range(len(first_eg)-1, 2019):
        if not first_eg[i] in first_eg[:i]:
            first_eg.append(0)
        else:
            last_occurence = max(loc for loc, val in enumerate(
                first_eg[:i]) if val == first_eg[i])
            first_eg.append(i-last_occurence)

    print("2020th word is", first_eg[-1], "   [O(n2)]")


def big_o_linear():
    # init
    second_eg = input.copy()
    occur_dict = {}
    for idx, sec in enumerate(second_eg[:-1]):
        occur_dict[sec] = idx

    # play game
    for i in range(len(second_eg)-1, 30000000-1):
        if not second_eg[i] in occur_dict:
            second_eg.append(0)
        else:
            second_eg.append(i-occur_dict.get(second_eg[i]))
        occur_dict[second_eg[i]] = i

        if(i % 2000000 == 0):
            print("Iter = ", "{:.1%}".format(i/30000000), end='\r')

    print("30.000.000th number is", second_eg[-1], "   [O(n)]")


lvl_runner(sys.argv, big_o_square, big_o_linear)
