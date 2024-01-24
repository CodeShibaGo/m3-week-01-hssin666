def disemvowel(s):
    s_novowel = str()
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        if s[i] in vowel_list:
            continue
        else:
            s_novowel += s[i]

    return s_novowel
