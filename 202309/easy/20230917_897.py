## https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root : return
        return self.make_answer(root, None)
    
    def make_answer(self, root, ans) :
        if root.right : ans = self.make_answer(root.right, ans)
        ans = TreeNode(root.val, None, ans)
        if root.left : ans = self.make_answer(root.left, ans)
        return ans