## https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None : return head

        self.node = ListNode(head.val)

        while head.next != None :
            if head.val == head.next.val :
                head.next = head.next.next
            else :
                self.node = self.addnode(head.next.val)
                head = head.next
                
        return self.node

    def addnode(self, value) :
        node = self.node
        while node.next : node = node.next
        node.next = ListNode(value)
        return self.node