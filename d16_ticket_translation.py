from utils import records_getter, lvl_runner
import sys
import re


def data_parser():
    data = records_getter("d16_input.txt")
    # Unpack rules
    rules = {}
    i = 0
    while data[i] != "":
        rule = re.findall(r'([\w\s]+):', data[i])
        values = re.findall(r'(\d+)\-(\d+)', data[i])
        rules[rule[0]] = [(int(tup[0]), int(tup[1])) for tup in values]
        i += 1
    # Unpack my ticket
    while data[i] != "your ticket:":
        i += 1
    i += 1
    my_ticket = [int(i) for i in data[i].split(',')]
    # Unpack nearby tickets
    while data[i] != "nearby tickets:":
        i += 1
    i += 1
    nearby_tickets = []
    for dat in data[i:]:
        nearby_tickets.append([int(i) for i in dat.split(',')])

    return rules, my_ticket, nearby_tickets


def first_lvl():
    rules, _, nearby_tickets = data_parser()
    invalid_sum = 0
    correct_tickets = []
    # flatten rules
    flatten_rules = []
    for t in list(rules.values()):
        flatten_rules.extend(t)

    for ticket in nearby_tickets:
        for val in ticket:
            for rule in flatten_rules:
                if rule[0] <= val <= rule[1]:
                    break
            else:
                invalid_sum += val
                break
        else:
            correct_tickets.append(ticket)
    return invalid_sum, correct_tickets


def second_lvl():
    _, correct_tickets = first_lvl()
    rules, my_ticket, _ = data_parser()
    rules_order = {}


def first_lvl_runner():
    print("Sum of invalid numbers:", first_lvl()[0])


second_lvl()
#lvl_runner(sys.argv, first_lvl_runner, second_lvl)
