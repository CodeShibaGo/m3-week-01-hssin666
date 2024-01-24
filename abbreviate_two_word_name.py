def abbrev_name(name):
    abbrev = [i[0] for i in name.split(' ')]
    result = abbrev[0] + '.' + abbrev[1]
    return result
