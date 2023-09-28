## https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.find_answer(root, 0, 0)

    def find_answer(self, root, tmp, ans) :
        tmp = (tmp*2) + root.val
        if not root.left and not root.right : ans += tmp
        if root.left : ans = self.find_answer(root.left, tmp, ans)
        if root.right : ans = self.find_answer(root.right, tmp, ans)
        return ans