# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

########
###  ###
##    ##

# Tags: Sets vs list!

##    ##
###  ###
########

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        d = set()
        for num in nums:
            if num not in d:
                d.add(num)
            else:
                output.append(num)
        return output
