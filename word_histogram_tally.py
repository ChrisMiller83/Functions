# Given a histogram tally (one returned from either letter_histogram or word_histogram), print the top 3 words or letters.
#$ python3 word_histogram_tally.py

#Please enter a sentence: To be or not to be do be do be do
#The top three words are:
#be: 4
#do: 3
#to: 2
user_input = input("Please give me a sentence.  ")

def word_count(string):
    counts = {}
    words = string.split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

word = top3_words(user_input)

def top3_words(words):
    new_list = words
    return((new_list))

print(top3_words(words))

        
