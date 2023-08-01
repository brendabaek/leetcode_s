## https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2, t1, t2 = l1.val, l2.val, 1, 1
        
        while l1.next != None :
            l1 = l1.next
            t1 *= 10
            num1 += l1.val * t1
        
        while l2.next != None :
            l2 = l2.next
            t2 *= 10
            num2 += l2.val * t2

        sums = num1 + num2
        return self.make_ListNode(sums)

    def make_ListNode(self, sums) :
        ans = ListNode(sums % 10)
        if sums // 10 > 0 :
            ans.next = self.make_ListNode(sums//10)
        return ans