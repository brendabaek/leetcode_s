## https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None : return
        
        root = head
        lst = [root.val]
        while root.next != None :
            root = root.next
            lst.append(root.val)
        
        k = k % len(lst)
        if k == 0 : return head
        lst = (lst[-k:]+lst[:len(lst)-k])[::-1]
        
        ans = None
        for l in lst :
            ans = ListNode(l, ans)
        return ans