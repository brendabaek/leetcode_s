## https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left == None and root.right == None : return 0
        elif root.left != None and root.right == None :
            cnt, ans = self.find_length(root.left, 0, 0)
            return max(cnt, ans)
        elif root.left == None and root.right != None :
            cnt, ans = self.find_length(root.right, 0, 0)
            return max(cnt, ans)
        else : ## root.left != None and root.right != None
            left, ans_left = self.find_length(root.left, 0, 0)
            right, ans_right = self.find_length(root.right, 0, 0)
            return max(ans_left, ans_right, left+right)

    def find_length(self, root, cnt, ans) :
        cnt += 1
        if root.left == None and root.right == None : return cnt, ans
        elif root.left != None and root.right == None :
            return self.find_length(root.left, cnt, ans)
        elif root.left == None and root.right != None :
            return self.find_length(root.right, cnt, ans)
        else : ## root.left != None and root.right != None
            left, ans_left = self.find_length(root.left, cnt, ans)
            right, ans_right = self.find_length(root.right, cnt, ans)
            if (left+right-cnt-cnt) > left and (left+right-cnt-cnt) > right :
                ans = max(ans_left, ans_right, (left+right-cnt-cnt))
                cnt = max(left, right)
                return cnt, ans
            else : return max(left, right), ans