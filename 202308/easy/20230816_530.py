## https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = self.cnt_node(root, [])
        lst.sort()

        ln = len(lst)
        ans = 10 ** 5
        for i in range(ln-1) :
            ans = min(ans, abs(lst[i+1] - lst[i]))
        return ans

    def cnt_node(self, root, lst) :
        lst.append(root.val)
        if root.left == None and root.right == None :
            return lst
        elif root.left != None and root.right == None :
            return self.cnt_node(root.left, lst)
        elif root.left == None and root.right != None :
            return self.cnt_node(root.right, lst)
        else : ## root.left == None and root.right == None :
            return self.cnt_node(root.right, self.cnt_node(root.left, lst))