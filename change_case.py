def change_case(input_str, case):
    if case == 'upper':
        result = input_str.upper()
    elif case == 'lower':
        result = input_str.lower()
    else:
        result = 'error'

    return result
