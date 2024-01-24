def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
        else:
            continue
    return result
