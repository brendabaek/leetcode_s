## https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if root == None : return
        return self.make_answer(root, '')

    def make_answer(self, root, ans) :
        ans += str(root.val)
        if root.left == None and root.right == None : return ans
        elif root.left != None and root.right == None :
            return self.make_answer(root.left, ans + '(') + ')'
        elif root.left == None and root.right != None :
            return self.make_answer(root.right, ans + '()(') + ')'
        else : ## root.left != None and root.right != None :
            ans = self.make_answer(root.left, ans + '(') + ')'
            return self.make_answer(root.right, ans + '(') + ')'