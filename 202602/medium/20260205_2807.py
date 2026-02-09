## https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            tmp = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = tmp
            curr = curr.next.next           
        return head

    def gcd(self, a, b):
        while b != 0: a, b = b, a % b
        return a