####
####12
####
#### Python Pocket Primer -
#### Exercises for chapter two
####
####
####

import sys

def print_clock():
    try:
        number = int(raw_input("Enter an hour number "))
        if number < 10:
            print('0'+str(number))
        elif number < 25:
            print(str(number))
        else:
            print('not a proper hour number')
    except ValueError:
        print('That is not a proper hour please try again')
        sys.exit()

def chart_creation():
    cal_num = range(0,10)
    for i in cal_num:
        print(i, i*i, i*i*i)

def chart_creation_odds():
    cal_num = range(0,10)
    for i in cal_num:
        if i % 2 != 0:
            print(i, i*i, i*i*i)

def chart_creation_prime():
    cal_num = range(0,10)
    i = 0
    prime = []
    while i < len(cal_num):
        for num in range(2,cal_num[i]):
            if i%num ==0:
                break
            else:
                if i in prime:
                    pass
                else:
                    prime.append(i)
        i = 1+i
    for i in prime:
        print(i,i*i,i*i*i)


def word_fun(words):
    words = words.split(' ')
    for i in words:
        print(i,i[::-1])

def word_fun_two(words):
    words = words.split(' ')
    max = ''
    min = 'ppppp'

    for i in words:
        if len(i)>len(max):
            max=i
        elif len(i)<len(min):
            min=i
        else:
            pass
    print(max, ' is longest word')
    print(min, ' is shortest word')

def find_the_word(word,array):
    array = array.split(' ')
    positions = []
    for index,i in enumerate(array):
        if i == word:
            if index % 2 ==0:
                positions.append(index)
            else:
                pass
    print(positions)

def plaindrome(word):
    if len(word) < 2:
        print('word is a plaindrome')
        return 'plaindrome'
    if word[0] != word[-1]:
        print('word is not a plaindrome')
        return False
    return plaindrome(word[1:-1])

def plaindrome_from_array(word):
    word = word.split(' ')
    plaindrome_words = []
    for i in word:
        if plaindrome(i) == 'plaindrome':
            plaindrome_words.append(i)
    if len(plaindrome_words)<1:
        print('you have no plaindromes')
    else:
        print(plaindrome_words)

def divided():
    array = range(1,101)
    for i in array:
        if i%3 == 0 or i%2==0:
            print(i)

def reverse_all(word):
    word = word.split(' ')
    word = word[::-1]
    final = []
    for i in word:
        i = i[::-1]
        final.append(i)
    print(final)

def test_perfect():
    nums = range(0,1000)
    count = 0
    for z in nums:

        divisors = []
        for i in range(1,z):
            if z%i ==0:
                divisors.append(i)
        divisors.append(z)
        if sum(divisors)==2*z:
            count = count + 1
            if count < 4:
                print('number ', z, ' is a perfect number', count)

def cap_first(list):
    list = list.split(' ')
    new_list = []
    for i in list:
        new_list.append(i.capitalize())
    print new_list
