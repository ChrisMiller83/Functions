def word_count(string):
    counts = {}
    words = string.split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
user_input = input("Please give me a sentence.  ")
print(word_count(user_input)) 