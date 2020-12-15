import sys
from utils import records_getter, lvl_runner


def any_one():
    lines = records_getter("d6_questionaire.txt")
    all_answers = ""
    total = 0
    for line in lines:
        if line == "":
            uniqe = []
            for a in all_answers:
                if a not in uniqe:
                    uniqe.append(a)
            answers_no = len(uniqe)
            total += answers_no
            # print(answers_no)
            all_answers = ""
        else:
            all_answers += line
    print("Anyone:", total)


def every_one():
    lines = records_getter("d6_questionaire.txt")
    team_member_answers = []
    total = 0
    for line in lines:
        if line == "":
            if len(team_member_answers) == 1:
                answers_no = len(team_member_answers[0])
            else:
                left_answers = team_member_answers[0]
                for tma in team_member_answers[1:]:
                    left_answers = [i for i in left_answers if i in tma]
                answers_no = len(left_answers)

            total += answers_no
            # print(answers_no)
            team_member_answers = []
        else:
            team_member_answers.append(line)

    print("Everyone:", total)


lvl_runner(sys.argv, any_one, every_one)
