## https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.find_answer(root, root.val)

    def find_answer(self, root, n) :
        if root.val != n: return False
        if root.left :
            if self.find_answer(root.left, n) == False : return False
        if root.right : return self.find_answer(root.right, n)
        return True