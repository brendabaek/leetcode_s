## https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned : return None
        return self.find_answer(cloned, target, False, None)[1]
    
    def find_answer(self, node, target, check, ans) :
        if check == True : return check, ans
        if node.val == target.val : return True, node
        if node.left : check, ans = self.find_answer(node.left, target, check, ans)
        if node.right : check, ans = self.find_answer(node.right, target, check, ans)
        return check, ans