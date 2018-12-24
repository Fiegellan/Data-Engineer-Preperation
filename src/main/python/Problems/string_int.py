# Implement atoi which converts a string to an integer.
# Take into account white spaces and if the final integer is positive or negative

# This can be significantly better than this first solution 


########
###  ###
##    ##

# Tags: Length of the string, checking arrays, retun answer

##    ##
###  ###
########

import unicodedata

class Solution(object):


    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        strip = str.lstrip()
        strip = strip.split(' ')
        print(strip)
        string = strip[0].encode('ascii','ignore')
        print(string)
        ans = ''
        if len(string)==0:
            return 0
        elif string[0].isalpha() and string[0] != '+' and string[0] != '-':
            print('issue')
            return 0
        elif not string[0].isdigit() and string[0] != '+' and string[0] != '-':
            return 0
        elif (string[0]=='+' or string[0]=='-' or int(string[0]) in range(0,10)):
            z=0
            ans_array = []
            if string[0]=='+' or string[0]=='-':
                strings =string[1:]
                if len(strings)==0:
                    return 0
                elif not strings[0].isdigit():
                    return 0
                print(strings)
            else:
                strings = string

            while z < len(strings):
                x = strings[z].encode('ascii','ignore')
                if x.isdigit():
                    if int(strings[z]) in range(0,11):
                        ans = ans + strings[z]
                        print(ans)
                else:
                    break
                z = z+1
        else:
            return 0

        answer = int(ans)

        if  -2147483648 < int(answer) < 2147483648:

            if string[0]=='+':
                answer = int(ans)
            elif string[0]=='-':
                answer = -int(ans)
                print(answer)
            else:
                answer = int(ans)

            return answer
        else:
            if string[0]=='-':
                return -2147483648
            else:
                return 2147483647
