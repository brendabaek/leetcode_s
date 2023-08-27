## https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None : return
        dics = self.make_answer(root, 0, {})
        return [(float(sum(v))/len(v)) for v in dics.values()]

    def make_answer(self, root, cnt, dics) :
        try : dics[cnt].append(root.val)
        except : dics[cnt] = [root.val]
        cnt += 1

        if root.left : dics = self.make_answer(root.left, cnt, dics)
        if root.right : dics = self.make_answer(root.right, cnt, dics)
        return dics