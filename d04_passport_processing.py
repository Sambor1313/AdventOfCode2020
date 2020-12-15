import re
import sys
from utils import records_getter, lvl_runner

lines = records_getter('d4_passports.txt')
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
fields_optional = ['cid']


def passport_veryfier(data):
    passport_data = re.findall(r"(\w+)\:(\#?\w+)+", data)
    passport_data_dict = dict(passport_data)
    # general validation
    for field in fields:
        if passport_data_dict.get(field) == None:
            return False
    # specyfi validation
    v = passport_data_dict.get('byr')
    if int(v) < 1920 or 2002 < int(v):
        return False
    v = passport_data_dict.get('iyr')
    if int(v) < 2010 or 2020 < int(v):
        return False
    v = passport_data_dict.get('eyr')
    if int(v) < 2020 or 2030 < int(v):
        return False
    v = re.findall(r"(\d+)\s*(\w+)", passport_data_dict.get('hgt'))
    if v:
        v = v[0]
    else:
        return False
    if(v[1] == 'cm'):
        if int(v[0]) < 150 or 193 < int(v[0]):
            return False
    else:
        if int(v[0]) < 59 or 76 < int(v[0]):
            return False
    v = re.findall(r"^\#[0-9a-f]{6}$", passport_data_dict.get('hcl'))
    if not v:
        return False
    v = re.findall(r"^(amb|blu|brn|gry|grn|hzl|oth)$",
                   passport_data_dict.get('ecl'))
    if not v:
        return False
    v = re.findall(r"^(\d{9})$",
                   passport_data_dict.get('pid'))
    if not v:
        return False
    return True


def passport_checker():
    handler = ""
    counter = 0
    all = 0
    for line in lines:
        if line == "":
            if passport_veryfier(handler):
                counter += 1
            all += 1
            handler = ""
        else:
            handler += (" " + line)
    print("Valid passports:", counter, " out of", all)


lvl_runner(sys.argv, None, passport_checker)
