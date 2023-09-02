## https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val, ans=None):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val : return root
        if root.left :
            ans = self.searchBST(root.left, val, ans)
            if ans : return ans
        if root.right :
            ans = self.searchBST(root.right, val, ans)
            if ans : return ans
        return ans