def is_square(n):
    if n < 0:
        result = False
    else:
        root = n**0.5
        result = root.is_integer()
    return result
