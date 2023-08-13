## https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root.val == None : return
        cnt = self.count_mode(root, {})
        m = max(cnt.values())
        ans = []
        for k, v in cnt.items() :
            if v == m : ans.append(k)

        return ans

    def count_mode(self, root, cnt) :
        if root.val in cnt : cnt[root.val] += 1
        else : cnt[root.val] = 1
        if root.left == None and root.right == None :
            return cnt
        elif root.left != None and root.right == None :
            return self.count_mode(root.left, cnt)
        elif root.left == None and root.right != None :
            return self.count_mode(root.right, cnt)
        else :
            cnt = self.count_mode(root.left, cnt)
            return self.count_mode(root.right, cnt)