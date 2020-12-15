import sys


def records_getter(file_name):
    """
    Inputs:
        file_name (string) - name of file in this directory to get rows

    Return:
        Rows (array) - array of strings as rows from file
    """
    rows = []
    with open(file_name, 'r') as file:
        data = file.read()
        rows = data.split('\n')
    return rows


def lvl_runner(arguments, first_lvl, second_lvl):
    '''
    Inputs:
        arguments - which func to run 1 or 2
        first_lvl - first function
        second_lvl - second function
    '''
    if len(arguments) == 2:
        if arguments[1] == '1':
            try:
                first_lvl()
            except:
                print("*** No first function ***")
            return
        elif arguments[1] == '2':
            try:
                second_lvl()
            except:
                print("*** No second function ***")
            return
    print('''    Run program with one argument: 
    1 or "first" or 2 or "second" to choose on part.
    ''')
