## https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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
        return self.make_answer(head, None, None, ListNode())

    def make_answer(self, head, tmp2, tmp1, ans) :
        if head == None :
            if tmp2 != None and tmp1 != None and tmp2 != tmp1 : return ListNode(tmp2, ListNode(tmp1))
            elif tmp2 != None and tmp1 == None : return ListNode(tmp2)
            else : return

        else :
            if tmp2 == None and tmp1 == None :
                ans = self.make_answer(head.next, head.val, None, ans)
            elif tmp2 != None and tmp1 == None:
                ans = self.make_answer(head.next, tmp2, head.val, ans)
            else :
                if tmp2 == tmp1 and tmp1 == head.val :
                    ans = self.make_answer(head.next, tmp2, tmp1, ans)
                elif tmp2 == tmp1 and tmp1 != head.val :
                    ans = self.make_answer(head.next, head.val, None, ans)
                elif tmp2 != tmp1 :
                    ans = ListNode(tmp2, self.make_answer(head.next, tmp1, head.val, ans))
        return ans