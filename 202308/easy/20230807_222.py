## https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None : return 0
        return self.count_node(root, 0)

    def count_node(self, root, ans):
        ans += 1
        if root.left == None and root.right == None :
            return ans
        elif root.left != None and root.right == None :
            return self.count_node(root.left, ans)
        elif root.left == None and root.right != None :
            return self.count_node(root.right, ans)
        elif root.left != None and root.right != None :
            ans = self.count_node(root.left, ans)
            return self.count_node(root.right, ans)