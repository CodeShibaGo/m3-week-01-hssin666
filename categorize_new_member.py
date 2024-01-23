def categorize_new_member(data):
    result = []
    for i in data:
        if i[0] >= 55 and i[1] >= 7:
            result.append('Senior')
        else:
            result.append('Open')
    return result
