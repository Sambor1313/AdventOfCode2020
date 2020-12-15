import sys
import re
from utils import records_getter, lvl_runner

# Creating a list of bags dicts


def creating_rules_list():
    rules = records_getter("d7_bags.txt")
    bags = []
    for rule in rules:
        r = rule.split(" bags contain ")
        r = dict(name=r[0], containing=re.findall(
            r"(\d+) (([\w\s]+) bags?)", r[1]))
        bags.append(r)
    return bags


def where_is_my_bag():
    # Where expect my (shiny gold) bag
    bags = creating_rules_list()
    containing_color = ["shiny gold"]
    new_bunch = 1
    old_bunch = 0

    while new_bunch > old_bunch:
        old_temp = old_bunch
        old_bunch = len(containing_color)
        for cc in containing_color[old_temp:]:
            for bag in bags:
                for ins in bag["containing"]:
                    if cc in ins:
                        containing_color.append(bag["name"])
        new_bunch = len(containing_color)
    # print(containing_color)
    print("As set:", len(set(containing_color))-1)


def how_many_bugs_to_buy():
    bags = creating_rules_list()
    containing_color = [(1, "shiny gold")]
    new_bunch = 1
    old_bunch = 0
    # How many bags in mine
    while new_bunch > old_bunch:
        old_temp = old_bunch
        old_bunch = len(containing_color)
        for cc in containing_color[old_temp:]:
            for br in bags:
                if br["name"] == cc[1]:
                    for b in br["containing"]:
                        containing_color.append((int(cc[0]) * int(b[0]), b[2]))
            new_bunch = len(containing_color)

    print(sum([i[0] for i in containing_color])-1)


lvl_runner(sys.argv, where_is_my_bag, how_many_bugs_to_buy)
