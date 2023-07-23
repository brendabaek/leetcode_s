## https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None : return
        lst = self.lst(root, [])
        ans = self.ans(lst, [])
        return ans

    def lst(self, root, lst):
        lst.append(root.val)
        if root.left != None and root.right == None :
            lst = self.lst(root.left, lst)
        elif root.left == None and root.right != None :
            lst = self.lst(root.right, lst)
        elif root.left != None and root.right != None :
            head_left = copy.deepcopy(lst)
            head_right = copy.deepcopy(lst)
            lst = [self.lst(root.left, head_left),  self.lst(root.right, head_right)]
        return lst

    def ans(self, lst, answer) :
        for i in lst :
            if type(i) == list :
                answer = self.ans(i, answer)
            else :
                txt = '->'.join(str(i) for i in lst)
                answer.append(txt)
                break

        return answer