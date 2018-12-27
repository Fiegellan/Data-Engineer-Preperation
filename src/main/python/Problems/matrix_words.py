# Given a dictionary, and a matrix of letters, find all the words in the matrix that are in the dictionary.
# Assumption - leeters in the list can be used more than once


word_matrix = {'all','and','mom','friend','clan'}
letters = ['a','l','m','o','m','c','n']
# letters = ['a']

words = []
for i in word_matrix:
    final = len(i)
    count = 0
    for z in i:
        if z in letters:
            count = count +1

    if count ==final:
        words.append(i)

if len(words)>0:
    print words
else:
    print 'no words possible'