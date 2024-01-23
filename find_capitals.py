def find_capitals(word):
    capital = str()
    for i in word.split(' '):
        if i.istitle():
            capital += i[0]
        else:
            continue
    return capital
