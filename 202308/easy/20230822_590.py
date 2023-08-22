## https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None : return
        return self.make_answer(root, [])

    def make_answer(self, root, ans):
        if root.children != None :
            for c in root.children :
                ans = self.make_answer(c, ans)
        ans.append(root.val)
        return ans
