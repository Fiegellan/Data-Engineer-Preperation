####
####
####
#### Python Pocket Primer -
#### Exercises for chapter one
#### Problems 1-5
####
####

def cel_to_far(c):
    far = c*(float(9)/float(5))+32
    return far

def far_to_cel(f):
    cel = (f-32)*(float(5)/float(9))
    return cel

def calculating_tempature():
    userInput = raw_input("are you converting to Farenheit? ")
    if userInput == 'yes':
        userInput = raw_input("What tempt will you like to convert to far?: ")
        print('You converted temp in Far is: ', cel_to_far(int(userInput)))
    else:
        userInput = raw_input("What tempt will you like to convert to cel?: ")
        print('You converted temp in Cel is: ', far_to_cel(int(userInput)))

def first_last_value():
    Strings= raw_input("please type a list, we will return the first an last value you enter")

    inputs = list(Strings)

    print('first value: ', inputs[1], 'last value: ', inputs[-1])

def print_first_word():
    words= raw_input("please type a list, we will return the word in the list you enter: ")
    print('your first word is: ' , words.split(' ')[0])

def plaindrome(word):
    if len(word) < 2:
        print('word is a plaindrome')
        return True
    if word[0] != word[-1]:
        print('word is not a plaindrome')
        return False
    return plaindrome(word[1:-1])


def test_five():
    pal = raw_input("please type some letters, will check if it's a palindrome: ")
    pal = pal[0:5]
    plaindrome(pal)


test_five()
