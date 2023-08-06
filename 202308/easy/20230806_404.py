## https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None : return 0
        return self.sum_left(root, 0)

    def sum_left(self, root, ans) :        
        if root.left != None and root.left.left == None and root.left.right == None :
            ans += root.left.val
        elif root.left != None : ans = self.sum_left(root.left, ans)
        if root.right != None : ans = self.sum_left(root.right, ans)
        return ans