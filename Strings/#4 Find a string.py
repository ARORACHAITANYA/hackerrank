import re
def count_substring(string, sub_string):
    s = [m.start() for m in re.finditer(f'(?={sub_string})', f'{string}')]
    return len(s)

