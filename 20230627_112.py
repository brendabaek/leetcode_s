## https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum) :
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root == None : return False
        else :
            sums = self.find_sums(root, targetSum)
            if sums == targetSum : return True
            else : return False

    def find_sums(self, root, targetSum, sums=0):
        sums += root.val

        if root.left == None and root.right != None :
            sums = self.find_sums(root.right, targetSum, sums)

        elif root.left != None and root.right == None :            
            sums = self.find_sums(root.left, targetSum, sums)
            
        elif root.left != None and root.right != None :
            left_sums = self.find_sums(root.left, targetSum, sums)
            right_sums = self.find_sums(root.right, targetSum, sums)

            if left_sums == targetSum : sums = left_sums
            else : sums = right_sums

        return sums