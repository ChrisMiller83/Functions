word1 = str(input("Please give me a word.  "))

def char_frequency(word1):
    dict = {}
    for n in word1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency(word1))