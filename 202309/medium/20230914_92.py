## https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head == None : return
        if head.next == None or left == right : return head
        return self.make_answer(head, left, right, 1, [])[1]

    def make_answer(self, head, left, right, cnt, lst) :
        if head.next != None:
            if left <= cnt and cnt <= right :
                lst.append(head.val)
                lst, head = self.make_answer(head.next, left, right, cnt+1, lst)
                if cnt == left :
                    for i in range(len(lst)) : head = ListNode(lst[i], head)
            else : ## cnt < left or right < cnt
                head = ListNode(head.val, self.make_answer(head.next, left, right, cnt+1, lst)[1])
        else :
            if cnt == right :
                lst.append(head.val)
                head = head.next
        return lst, head