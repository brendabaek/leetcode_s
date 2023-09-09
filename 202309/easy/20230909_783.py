## https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst, ans = self.make_lst(root, []), 10**5
        lst.sort()
        for i in range(len(lst)-1) : ans = min(ans, lst[i+1]-lst[i])
        return ans

    def make_lst(self, root, lst) :
        lst.append(root.val)
        if root.left : self.make_lst(root.left, lst)
        if root.right : self.make_lst(root.right, lst)
        return lst