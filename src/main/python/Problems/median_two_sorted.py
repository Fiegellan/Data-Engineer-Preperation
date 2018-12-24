# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays.

########
###  ###
##    ##

# Tags: Odd VS Even - floats and array fun

##    ##
###  ###
########

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_num = sorted(nums1+nums2)
        print new_num
        # Check if they the merged array is odd or even in length
        if len(new_num)%2 !=0:
            print 'no'
            return new_num[len(new_num)/2]
        else:
            print (float(new_num[len(new_num)/2])+float(new_num[len(new_num)/2-1]))/2
            return (float(new_num[len(new_num)/2])+float(new_num[len(new_num)/2-1]))/2
