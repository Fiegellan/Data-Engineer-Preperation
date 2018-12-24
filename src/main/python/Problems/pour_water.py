# We are given an elevation map, heights[i] representing the height of the terrain at that index.
# The width at each index is 1. After V units of water fall at index K, how much water is at each index?
#
# Water first drops at index K and rests on top of the highest terrain or water at that index.
# Then, it flows according to the following rules:

# If the droplet would eventually fall by moving left, then move left.
# Otherwise, if the droplet would eventually fall by moving right, then move right.
# Otherwise, rise at it's current position.


########
###  ###
##    ##

# Tags: Checking right and left, keeping track of array location, keeping height

##    ##
###  ###
########


class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for z in range(V):
            l = r = K
            for i in range(K - 1, -1, -1):
                if heights[i] > heights[l]:
                    break
                elif heights[i] < heights[l]:
                    l = i
            if l < K:
                heights[l] += 1
            else:
                for j in range(K + 1, len(heights)):
                    if heights[j] > heights[r]:
                        break
                    elif heights[j] < heights[r]:
                        r = j
            if l == r == K:
                heights[K] += 1
            elif r > K:
                heights[r] += 1
        return heights
