def greet(name):
    if name == 'Johnny':
        result = "Hello, my love!"
    else:
        # result = "Hello, {}!".format(name)
        result = f"Hello, {name}!"

    return result
