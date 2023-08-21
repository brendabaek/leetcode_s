## https://leetcode.com/problems/n-ary-tree-preorder-traversal/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None : return
        return self.make_answer(root, [])

    def make_answer(self, root, ans) :
        ans.append(root.val)
        if root.children :
            for r in root.children :
                self.make_answer(r, ans)
        return ans
      