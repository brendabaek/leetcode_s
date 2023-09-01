## https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA.val == None or headB.val == None : return
        
        lstA = self.make_lst(headA)
        lstB = self.make_lst(headB)
        lnA = len(lstA)
        lnB = len(lstB)
        ln = min(lnA, lnB)
        cnt = None

        for i in range(-1, -ln-1, -1) :
            if lstA[i] == lstB[i] : cnt = i
            else : break        

        if cnt == None : return

        newA = self.new_head(headA, lnA+cnt)
        newB = self.new_head(headB, lnB+cnt)
        
        for i in range(-cnt) :
            if newA == newB : return newA
            else :
                newA = newA.next
                newB = newB.next
        

    def make_lst(self, root) :
        ans = []
        while True :
            ans.append(root.val)
            if root.next != None : root = root.next
            else : return ans

    def new_head(self, root, cnt) :
        for i in range(cnt) : root = root.next
        return root