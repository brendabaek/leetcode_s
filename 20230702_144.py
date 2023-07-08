## https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if root == None : return ans
        return  self.find_nums(root, ans)
    
    def find_nums(self, root, ans) :
        ans.append(root.val)
        if root.left == None and root.right == None : return ans
        elif root.left != None and root.right == None :
            return self.find_nums(root.left, ans)
        elif root.left == None and root.right != None :
            return self.find_nums(root.right, ans)
        else : ## root.left != None and root.right != None
            ans = self.find_nums(root.left, ans)
            ans = self.find_nums(root.right, ans)
            return ans