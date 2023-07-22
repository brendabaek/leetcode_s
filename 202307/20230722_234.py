## https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None : return

        lst = [head.val]
        while head.next != None :
            head = head.next
            lst.append(head.val)

        ln = len(lst)
        for i in range(ln//2) :
            if lst[i] != lst[ln-1-i] :
                return False

        return True