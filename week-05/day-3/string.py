def string_x(string):
    if len(string) == 0:
        return string
    if string[0] == 'x':
        return 'y' + string_x(string[1:])
    return string[0] + string_x(string[1:])

def no_x(string):
    if len(string) == 0:
        return string
    if string[0] == 'x' or string[0] == 'X':
        return no_x(string[1:])
    return string[0] + no_x(string[1:])

def add_asterisk(string):
    if len(string) == 1:
        return string
    else:
        return string[0] + '*' + add_asterisk(string[1:])
