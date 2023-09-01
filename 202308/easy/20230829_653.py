## https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root : return
        lst = self.make_lst(root, [])
        lst.sort()
        
        for i in range(len(lst)-1) :
            for j in range(len(lst)-1, i, -1) :
                if lst[i] + lst[j] == k : return True
                elif lst[i] + lst[j] < k : break
        return False
        
    def make_lst(self, root, lst) :
        lst.append(root.val)
        if root.left :
            lst = self.make_lst(root.left, lst)
        if root.right :
            lst = self.make_lst(root.right, lst)
        return lst