## https://leetcode.com/problems/root-equals-sum-of-children/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, True)

    def check(self, node, ans) :
        if ans == False : return False
        if node.left == None and node.right == None : return ans
        if node.val != node.left.val + node.right.val : return False
        if node.left != None : ans = self.check(node.left, ans)
        if ans == True and node.right != None : self.check(node.right, ans)
        return ans