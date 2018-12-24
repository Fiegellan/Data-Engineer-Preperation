# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

########
###  ###
##    ##

# Tags: Reverse sort

##    ##
###  ###
########

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = sorted(nums, reverse = True)
        print a
        return a[k-1]
