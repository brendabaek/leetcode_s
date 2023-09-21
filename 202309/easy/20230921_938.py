## https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high, ans=0):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root : return ans
        if root.val < low : ans = self.rangeSumBST(root.right, low, high, ans)
        if high < root.val : ans = self.rangeSumBST(root.left, low, high, ans)
        if low <= root.val and root.val <= high :
            ans += root.val
            ans = self.rangeSumBST(root.right, low, high, ans)
            ans = self.rangeSumBST(root.left, low, high, ans)
        return ans