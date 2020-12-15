import re
import subprocess
from pathlib import Path
from colorama import Fore, Back, Style


def main():
    """
    This is main function in app. Run console basic program.
    """
    # Initialization parameters
    commands = {'e': 'exit - end program',
                'toc': 'table of content',
                'h': 'help/commands',
                'd': 'running programs submenu',
                'd##': 'run program of day ##',
                'd##-?': '? -> 1 or 2 for run part of day'}
    days = days_getter()

    # Print start screen
    print_welcome()

    # Program loop
    while True:
        inp = input(f'''\n{Fore.GREEN}What next? ;)   
    -> {Fore.RESET}''')
        inp.lower()
        if inp == "e":
            print_goodbye()
            break
        elif inp == "toc":
            print_toc(days)
        elif inp == "h" or inp == "help":
            print_command_list(commands)
        elif inp[0] == 'd':
            # Getting d##-? input
            if len(inp) == 1:
                prg_number = input(f'''    Which program would you like to test? 
    Choose from 1 to {len(days)}
    You can also add ##-? dash and 1/2 for run only first or second part of day.
    {Fore.GREEN}->{Fore.RESET} ''')
                prg_number = prg_number.split('-')
            else:
                prg_number = inp[1:].split('-')

            if len(prg_number) == 1:
                prg_number.append('0')
            else:
                if not (prg_number[1] == '1' or prg_number[1] == '2'):
                    prg_number[1] = '0'

            prg_number[0] = "{0:0>2}".format(prg_number[0])
            # Execute
            day_path = next((item['path'] for item in days
                             if item["id"] == prg_number[0]), None)
            if day_path == None:
                print("***There is no such day solved***")
            else:
                if prg_number[1] == '0' or prg_number[1] == '1':
                    print(
                        f"{Style.BRIGHT}Day {Fore.CYAN}{prg_number[0]}{Fore.RESET} result of {Fore.CYAN}1st{Fore.RESET} part{Style.RESET_ALL}")
                    subprocess.run([day_path, '1'], shell=True)
                if prg_number[1] == '0' or prg_number[1] == '2':
                    print(
                        f"{Style.BRIGHT}Day {Fore.CYAN}{prg_number[0]}{Fore.RESET} result of {Fore.CYAN}2nd{Fore.RESET} part{Style.RESET_ALL}")
                    subprocess.run([day_path, '2'], shell=True)
        else:
            print(
                f"      {Fore.RED}...*** There no command as \"{inp}\" ***...{Fore.RESET}")
            print_command_list(commands)


def print_command_list(commands):
    """
    Printing all commands with description in this program.
    """
    print(
        f'''
     ________{Fore.GREEN}LIST OF COMMANDS{Fore.RESET}______________________
    |  {Fore.RED}Command{Fore.RESET}  |            {Fore.RED}Description{Fore.RESET}           |
    |-----------|----------------------------------| '''
    )
    for com in commands:
        print(
            f"    |{com.center(11)}|{commands[com].center(34)}|")
    print("    |______________________________________________|")


def print_toc(days):
    """
    Printing all quests/programs realised in 2020 challange.
    """

    print(
        f'''
     ________{Fore.BLUE}LIST OF QUESTS{Fore.RESET}_____________________________
    |{Fore.BLUE}{'Day'.center(34)}{Fore.RESET}| {Fore.MAGENTA}First{Fore.RESET} | {Fore.MAGENTA}Second{Fore.RESET} |
    |----------------------------------|-------|--------| '''
    )
    for d in days:
        print(
            f"    |{d['id'].center(6)}|{d['name'].center(27)}|   *   |{'*'.center(8) }|")
    print("    |______|___________________________|_______|________|")


def print_welcome():
    """
    Printing welcome text
    """
    print('''
                ===.
        =====.==`.               __,------._
            ===`.8=);   _/)    .-'           ``-.
            _ (G^ @@__ / '.  .' By Toutatis, the `.
    ,._,-'_`-/,-^( _).__: .' druid's potion made :
    (    / .MMm.Y_)/      ,'  me strong enought    |
    `'(|.oMMMM       __,',-'`.  to solve this    ,'
    d88:'mOom        `--'     '. AdventOfCode!_-'
    88::(::\d88b                `-..______,--'
    Y88  ':88888
    _________888P__________________________________________________osfa
    |                                                              |
    |    Welcome in my version of Advent Of Code 2020 adventure.   |
    |                                         ~~Sambor1313         |
    |______________________________________________________________|

(h for help)    ''')


def print_goodbye():
    """
    Print goodbye message
    """
    print(
        '''

                                              --     --
                                            .:"  | .:'" |
                                          -- ___   ___ -
    Goodbye;)                          /:.  /  .\ / .  \.'.
    I hope you enjoy my results.      |:|. ;\___/O\___ /  :|
    I invite you to review            |:|. |  `__|__'   | .|
    my code on github.                |:|.  \_,     , _ /  /
                                       \______         |__/
    Goodbye!                             |:.           '.
    @Sambor1313                         /.:,|  |        ',
                                       /.:,.|  |         ',
                                       |::.. \_;_\-;       |
                                 _____|::..    .::|       |
                                /   ----,     .::/__,    /__,
                                \_______|,...____;_;_|../_;_|
    ''')


def days_getter():
    path = Path('')
    days = [d for d in path.glob("*.py") if str(d)[0] == "d"]
    days_return = []
    for day in days:
        d_temp = re.findall(r"^d(\d+)_([\w_]+).py", str(day))[0]
        days_return.append({'id': d_temp[0], 'name': d_temp[1], 'path': day})
    return days_return


main()
