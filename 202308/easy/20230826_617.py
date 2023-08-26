## https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 == None : return root2
        elif root2 == None : return root1
        return self.make_answer(root1, root2, TreeNode())

    def make_answer(self, root1, root2, ans) :
        ans.val = root1.val + root2.val

        if root1.left != None and root2.left != None :
            ans.left = self.make_answer(root1.left, root2.left, TreeNode())
        elif root1.left != None and root2.left == None :
            ans.left = root1.left
        elif root1.left == None and root2.left != None :
            ans.left = root2.left

        if root1.right != None and root2.right != None :
            ans.right = self.make_answer(root1.right, root2.right, TreeNode())
        elif root1.right != None and root2.right == None :
            ans.right = root1.right
        elif root1.right == None and root2.right != None :
            ans.right = root2.right

        return ans