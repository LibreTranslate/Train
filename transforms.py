
def remove_unpaired_quotes_and_brackets(line):
    # Deleting unpaired quotation marks
    if (line.count('“') + line.count('”')) % 2 != 0:
        line = line.replace('“', '')
        line = line.replace('”', '')
    if (line.count('«') + line.count('»')) % 2 != 0:
        line = line.replace('«', '')
        line = line.replace('»', '')
    while line.count('"') % 2 != 0:
        line = line.replace('"', '', 1)
    # Deleting unpaired square brackets
    while line.count('[') != line.count(']'):
        if '[' in line:
            line = line.replace('[', '', 1)
        if ']' in line:
            line = line.replace(']', '', 1)
    # Deleting unpaired parentheses
    while line.count('(') != line.count(')'):
        if '(' in line:
            line = line.replace('(', '', 1)
        if ')' in line:
            line = line.replace(')', '', 1)
    # Deleting unpaired curly braces
    while line.count('{') != line.count('}'):
        if '{' in line:
            line = line.replace('{', '', 1)
        if '}' in line:
            line = line.replace('}', '', 1)
    return line

def remove_chars(line, chars = []):
    for c in chars:
        line = line.replace(c, '')
    return line