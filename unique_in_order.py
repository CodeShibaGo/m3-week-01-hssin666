def unique_in_order(iterable):
    if len(iterable) == 0:
        result =[]
    else:
        result = [iterable[0]]
        for i in iterable:
            if i != result[-1]:
                result.append(i)
            else:
                continue
    return result
