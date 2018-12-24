# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

########
###  ###
##    ##

# Tags: Reverse, Linked List, Maps

##    ##
###  ###
########


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        l1l = []
        l2l = []
        while l1 != None:
            print (l1.val)
            l1l.append(l1.val)
            l1 = l1.next
        while l2 != None:
            print (l2.val)
            l2l.append(l2.val)
            l2 = l2.next

        l1r = list(reversed(l1l))
        l2r = list(reversed(l2l))
        num1 = int(''.join(map(str,l1r)))
        num2 = int(''.join(map(str,l2r)))
        final_num = num1 + num2
        print(final_num)

        split_final = [int(d) for d in str(final_num)]
        splitr = list(reversed(split_final))
        print(splitr)
        return splitr
