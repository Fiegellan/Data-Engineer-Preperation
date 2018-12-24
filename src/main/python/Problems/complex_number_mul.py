# Given two strings representing two complex numbers.

# You need to return a string representing their multiplication. Note i2 = -1 according to the definition.


class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        a_2 = int(str(a[1]).replace('i',''))
        b_2 = int(str(b[1]).replace('i',''))

        first = int(a[0])*int(b[0])
        second = int(a[0])*b_2 + int(b[0])*a_2
        third = a_2*b_2*-1
        final = str(first + third) + '+'+str(second)+'i'
        return final
