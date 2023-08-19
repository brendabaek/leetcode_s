## https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None : return 0
        return self.find_maximum(root, 0, 0)
        
    def find_maximum(self, root, cnt, ans):
        cnt += 1
        if root.children == [] : return max(cnt, ans)
        for c in root.children :
            nxt_cnt = cnt
            ans = self.find_maximum(c, nxt_cnt, ans)
        return ans