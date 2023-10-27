## https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.make_answer(1, n)

    def make_answer(self, stt, end) :
        if stt > end : return [None]
        ans = []
        for i in range(stt, end+1) :
            left = self.make_answer(stt, i-1)
            right = self.make_answer(i+1, end)
            for l in left :
                for r in right :
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ans.append(root)
        return ans
