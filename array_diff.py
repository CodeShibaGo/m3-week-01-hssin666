def array_diff(a, b):
    # result = list((set(a))-set(b) | (set(b)-set(a))
    intersec = list(set(a) & set(b))
    result = []
    for j in a:
        if j not in intersec:
            result.append(j)

    return result
