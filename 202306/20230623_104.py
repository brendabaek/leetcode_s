## https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None : return 0
        elif root.left == None and root.right == None : return 1
        else :
            depth = 0
            return self.search_depth(root, depth)
    
    def search_depth(self, node, depth) :
        depth += 1
        if node.left == None and node.right == None :
            return depth
        elif node.left == None and node.right != None :
            return self.search_depth(node.right, depth)
        elif node.left != None and node.right == None :
            return self.search_depth(node.left, depth)
        elif node.left != None and node.right != None :
            left_depth = self.search_depth(node.left, depth)
            right_depth = self.search_depth(node.right, depth)
            depth = max(left_depth, right_depth)
            return depth