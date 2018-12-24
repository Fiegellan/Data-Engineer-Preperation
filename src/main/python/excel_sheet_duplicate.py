# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# What is helpful here - open excel and look at how they do the number compared to the alpha code
# From there you can look at the logic and see how it's created


########
###  ###
##    ##

# Tags: Dictionary, string manipulation,

##    ##
###  ###
########


import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d = dict(enumerate(string.ascii_lowercase, 1))
        answer = ''
        if n < 27:
            return d[n].upper()
        else:
            while n > 0:
                n, r = divmod(n, 26)
                if r == 0:
                    n = n-1
                    r = r + 26
                answer=d[r].upper() + answer
        return answer
