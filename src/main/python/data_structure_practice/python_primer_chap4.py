####
####
####
#### Python Pocket Primer -
#### Exercises for chapter two
####
####
####

import sys

def wordPlay(list):
    vowel = ['a','e','i','o','u']
    list = list.split(' ')
    v_list = []
    for i in list:
        if i[0] in vowel or i[-1] in vowel:
            v_list.append(i)
    dic ={}
    for i in v_list:
        z = 0
        cnt = 0
        while z < len(list):
            if i == list[z]:
                cnt = cnt + 1
            dic[i]=cnt
            z = z +1
    print(dic)

def wordCount(word):
    word = word.split(' ')
    for i in word:
        if len(i)<5:
            z = range(1,len(i)+1)
            for x in z:
                print(i[0:x])

wordCount('hello my name something or other')
