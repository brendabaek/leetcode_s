## https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        ans_x, mom_x, cnt_x = self.find_answer(root, x, None, 0, False)
        ans_y, mom_y, cnt_y = self.find_answer(root, y, None, 0, False)
        if mom_x == mom_y : return False
        else : return cnt_x == cnt_y

    def find_answer(self, root, n, mom, cnt, ans) :
        if ans == True : return ans, mom, cnt
        if root.val == n : return True, mom, cnt
        mom = root.val
        if root.left : ans, mom_left, cnt_left = self.find_answer(root.left, n, mom, cnt+1, ans)
        if ans == True : return ans, mom_left, cnt_left
        if root.right : ans, mom_right, cnt_right = self.find_answer(root.right, n, mom, cnt+1, ans)
        if ans == True : return ans, mom_right, cnt_right
        return ans, mom, cnt