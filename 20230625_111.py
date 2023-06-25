## https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None : return True
        else :
            ans, cnt = self.check_root(root)
            return ans

    def check_root(self, root, cnt=0, ans=True) :
        if root.left == None and root.right == None : return True, cnt
        elif root.left == None and root.right != None :
            cnt += 1
            if root.right.left == None and root.right.right == None : return True, cnt
            else : return False, cnt
        elif root.left != None and root.right == None :
            cnt += 1
            if root.left.left == None and root.left.right == None : return True, cnt
            else : return False, cnt
        elif root.left != None and root.right != None :
            cnt += 1
            left_ans, left_cnt = self.check_root(root.left, cnt)
            right_ans, right_cnt = self.check_root(root.right, cnt)
            cnt = max(left_cnt, right_cnt)

            if left_ans == False or right_ans == False : return False, cnt
            elif abs(left_cnt - right_cnt) > 1 : return False, cnt
            else : return True, cnt