## https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        print(head)

        if head == None or head.next == None : return False

        check = head

        while head.next != None and check.next != None and check.next.next != None :
            head = head.next
            check = check.next.next
            if head == check : return True

        return False