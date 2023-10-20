## https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        while head.val == 0 and head.next : head = head.next
        if head == None or head.val == 0 : return 0
        ans = 1
        while head.next :
            head = head.next
            ans = ans*2 + head.val
        return ans