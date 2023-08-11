## https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.val == None : return
        head, cnt = self.remove_n(head, n, 1)
        return head

    def remove_n(self, head, n, cnt) :
        if head.next != None : head.next, cnt = self.remove_n(head.next, n, cnt)
        if n < cnt : return head, cnt
        elif n == cnt : return head.next, cnt+1
        else : return head, cnt+1