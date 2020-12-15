import sys
import re
from utils import records_getter, lvl_runner


def oldPass():
    passwords = records_getter('d2_passwords.txt')
    correct_passwords = 0
    for passw in passwords:
        l_lim, h_lim, letter, code = re.findall(
            "^(\d+)-(\d+)\s(\w):\s(\w+)$", passw)[0]
        occurs = code.count(letter)
        if int(l_lim) <= occurs <= int(h_lim):
            correct_passwords += 1
    print("Old password is:", correct_passwords)


def newPass():
    passwords = records_getter('d2_passwords.txt')
    correct_passwords = 0
    for passw in passwords:
        l_lim, h_lim, letter, code = re.findall(
            "^(\d+)-(\d+)\s(\w):\s(\w+)$", passw)[0]
        if (code[int(l_lim)-1] == letter) ^ (code[int(h_lim)-1] == letter):
            correct_passwords += 1
    print("New password is:", correct_passwords)


lvl_runner(sys.argv, oldPass, newPass)
