

def is_method(line):
    if (line.__contains__('public') or line.__contains__('private')) \
            and (line.__contains__('(')) and (line.__contains__(')')) and not (line.__contains__('class')):
        return True
    else:
        return False

def get_accessor(line):
    return line.strip().replace('{','').split(' ')[0].replace(';', '')

def get_type(line):
    return line.strip().replace('{','').split(' ')[1]

def get_method_name(line):
    return line.strip().replace('{','').split(' ')[2].split('(')[0]

def get_signature(line):
    signature = line.strip().split('(')[1].replace(')','').replace('{','')
    return signature