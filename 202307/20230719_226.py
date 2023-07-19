## https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None : return
        return self.answer(root)
    
    def answer(self, root) :
        ans = TreeNode()
        ans.val = root.val
        if root.left != None and root.right == None :
            ans.right = self.answer(root.left)
        elif root.left == None and root.right != None :
            ans.left = self.answer(root.right)
        elif root.left != None and root.right != None :
            ans.right = self.answer(root.left)
            ans.left = self.answer(root.right)
        return ans