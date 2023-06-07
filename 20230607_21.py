## https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        lst = []

        while list1 :
            lst.append(list1.val)
            list1 = list1.next

        while list2 :
            lst.append(list2.val)
            list2 = list2.next

        ln = len(lst)
        lst.sort()

        if ln == 0 : return list1
        elif ln == 1 :
            return ListNode(lst[0])
        else :
            self.val = ListNode(lst[0])
            for i in range(1, ln) :
                self.val = self.addnode(lst[i])
            return self.val

    def addnode(self, value) :
        node = self.val
        while node.next : node = node.next
        node.next = ListNode(value)
        return self.val    