## https://leetcode.com/problems/subtree-of-another-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None : return False
        return self.find_answer(root, subRoot, False)

    def find_answer(self, root, subRoot, ans) :
        if root.val == subRoot.val : ans = self.check_answer(root, subRoot, True)
        if ans == True : return True
        if root.left == None and root.right == None :
            return ans
        elif root.left != None and root.right == None :
            return self.find_answer(root.left, subRoot, ans)
        elif root.left == None and root.right != None :
            return self.find_answer(root.right, subRoot, ans)
        else : ## root.left != None and root.right != None
            if self.find_answer(root.left, subRoot, ans) == True :return True
            return self.find_answer(root.right, subRoot, ans)
    
    def check_answer(self, root, subRoot, ans) :
        if root.val != subRoot.val or ans == False : return False
        if root.left == None and root.right == None and subRoot.left == None and subRoot.right == None :
            return True
        elif root.left != None and root.right == None and subRoot.left != None and subRoot.right == None :
            return self.check_answer(root.left, subRoot.left, ans)
        elif root.left == None and root.right != None and subRoot.left == None and subRoot.right != None :
            return self.check_answer(root.right, subRoot.right, ans)
        elif root.left != None and root.right != None and subRoot.left != None and subRoot.right != None :
            if self.check_answer(root.left, subRoot.left, ans) == False : return False
            return self.check_answer(root.right, subRoot.right, ans)
        else : return False