

def is_method(line):
    if (line.__contains__('public') or line.__contains__('private')) \
            and (line.__contains__('(')) and (line.__contains__(')')) and not (line.__contains__('class')):
        return True
    else:
        return False