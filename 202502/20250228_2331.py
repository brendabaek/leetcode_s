## https://leetcode.com/problems/evaluate-boolean-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.calc(root) == 1

    def calc(self, node) :
        if node.left == None and node.right == None : return node.val
        if node.left.val in [2, 3] : node.left.val = self.calc(node.left)
        if node.right.val in [2, 3]: node.right.val = self.calc(node.right)
        return node.left.val or node.right.val if node.val == 2 else node.left.val and node.right.val