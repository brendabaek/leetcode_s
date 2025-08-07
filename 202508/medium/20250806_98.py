## https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left:
            if self.rootcheck(root.left, -2 ** 31 - 1, root.val) == False: return False
        if root.right: return self.rootcheck(root.right, root.val, 2 ** 31)
        return True

    def rootcheck(self, root, mini, maxi):
        if root.val <= mini or root.val >= maxi: return False
        if root.left:
            if self.rootcheck(root.left, mini, root.val) == False: return False
        if root.right: return self.rootcheck(root.right, root.val, maxi)
        return True