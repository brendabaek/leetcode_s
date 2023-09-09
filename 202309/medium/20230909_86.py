## https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head == None : return
        left, right = self.make_lst(head, x, None, None)
        if left == None : return right
        elif right == None : return left
        else : return self.make_answer(left, right)

    def make_lst(self, head, x, left, right) :
        if head.next : left, right = self.make_lst(head.next, x, left, right)
        if head.val < x : left = ListNode(head.val, left)
        else : right = ListNode(head.val, right)
        return left, right

    def make_answer(self, left, right) :
        if left.next == None : left.next = right
        else : left.next = self.make_answer(left.next, right)
        return left