## https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cnt, node = 1, head
        while node.next :
            cnt += 1
            node = node.next
        cnt = cnt//2
        while cnt > 0 :
            cnt -= 1
            head = head.next
        return head