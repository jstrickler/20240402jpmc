from itertools import groupby

with open('../DATA/words.txt') as words_in:  # open file for reading
    # create generator of all words, stripped of the trailing '
    all_words = [w.rstrip() for w in words_in]  

    # create a groupby() object where the key is the first character in the word
groups = groupby(all_words, key=lambda e: e[0])  

for letter, group in groups:
    print(letter, len(list(group)))




