## https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None or val == None : return
        return self.answer(head, val)

    def answer(self, head, val) :
        node = ListNode()
        while head.next != None :
            if head.val != val :
                node.val = head.val
                head = head.next
                node.next = self.answer(head, val)
                return node
            else : head = head.next
        
        if head.next == None :
            if head.val != val :
                node.val = head.val
                return node
            else : return