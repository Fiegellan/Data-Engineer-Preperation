####
####12
####
#### Python Pocket Primer -
#### Exercises for chapter two
####
####
####

import sys

def count_words(word):
    word = word.split(' ')
    words = [x.strip(' ') for x in word]
    count = {}
    for i in words:
        z = 0
        cnt = 0
        while z < len(words):
            if i.strip() == words[z]:
                cnt = cnt + 1
            z = z + 1
        count[i]=cnt
    print(count)


def show_lists(lists):
    for i in lists:
        if type(i)==list:
            print i

count_words('hello my name is yo momma hello')

#bam = ['hello','yes','3',[1,2,3],'by',['a','b']]=
#show_lists(bam)
