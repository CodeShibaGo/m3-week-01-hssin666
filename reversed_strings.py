def reverse_string(s):
    s_rev = str()
    for i in range(len(s)):
        s_rev += s[-(i + 1)]

    return s_rev
