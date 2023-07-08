## https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        

        if root == None : return root
        ans = []
        return self.add_values(root, ans)
        
    def add_values(self, root, ans) :
        if root.left != None : self.add_values(root.left, ans)
        ans.append(root.val)
        if root.right != None : self.add_values(root.right, ans)
        return ans