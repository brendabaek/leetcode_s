## https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None : return
        return self.answer(head)
    
    def answer(self, head) :
        node = ListNode(head.val)
        while head.next != None :
            head = head.next
            node = ListNode(head.val, node)
        return node