## https://leetcode.com/problems/leaf-similar-trees/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2 : return False
        lst1, lst2 = self.make_lst(root1, []), self.make_lst(root2, [])
        return lst1 == lst2
    
    def make_lst(self, root, ans) :
        if root.val == None : return ans
        if not root.left and not root.right : ans.append(root.val)
        if root.left : ans = self.make_lst(root.left, ans)
        if root.right : ans = self.make_lst(root.right, ans)
        return ans