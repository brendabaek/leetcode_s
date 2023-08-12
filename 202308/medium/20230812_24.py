## https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.make_answer(head)

    def make_answer(self, head) :
        try :
            if head.next.next != None : self.make_answer(head.next.next)
        except : pass
        try :
            if head.next != None :head.val, head.next.val = head.next.val, head.val
        except : pass
        return head       