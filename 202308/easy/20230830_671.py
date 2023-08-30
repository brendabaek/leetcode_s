## https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root) or (not root.left) : return -1
        lst = self.make_lst(root, [])
        m = min(lst)
        while True :
            try : lst.remove(m)
            except :
                if lst : return min(lst)
                else : return -1

    def make_lst(self, root, lst) :
        lst.append(root.val)
        if root.left : lst = self.make_lst(root.left, lst)
        if root.right : lst = self.make_lst(root.right, lst)
        return lst