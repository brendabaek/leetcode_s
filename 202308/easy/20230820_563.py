## https://leetcode.com/problems/binary-tree-tilt/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None : return 0
        s, ans = self.make_list(root, 0, 0)
        return ans

    def make_list(self, root, s, ans) :
        if root.left == None and root.right == None : pass
        elif root.left != None and root.right == None :
            s, ans = self.make_list(root.left, s, ans)
            ans = ans + abs(s)
        elif root.left == None and root.right != None :
            s, ans = self.make_list(root.right, s, ans)
            ans = ans + abs(s)
        elif root.left != None and root.right != None :
            left_s, left_ans = self.make_list(root.left, s, ans)
            right_s, right_ans = self.make_list(root.right, s, ans)
            s = s + left_s + right_s
            ans = ans + left_ans + right_ans + abs(left_s - right_s)
        s += root.val
        return s, ans