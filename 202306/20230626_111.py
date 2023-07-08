## https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None : return 0
        else :
            cnt = 0
            return self.node_depth(root, cnt)


    def node_depth(self, root, cnt) :
        cnt += 1
        if root.left == None and root.right == None : return cnt
        elif root.left == None and root.right != None :
            return self.node_depth(root.right, cnt)
        elif root.left != None and root.right == None :
            return self.node_depth(root.left, cnt)
        elif root.left != None and root.right != None :
            left_cnt = self.node_depth(root.left, cnt)
            right_cnt = self.node_depth(root.right, cnt)
            cnt = min(left_cnt, right_cnt)
            return cnt
