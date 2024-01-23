def count_duplicates(text):
    # count = {}
    # for i in text:
    #    count[i] += 1
    count = []
    word = []
    for i in text.lower():
        if i not in word:
            word.append(i)
        else:
            count.append(i)
    return len(set(count))
