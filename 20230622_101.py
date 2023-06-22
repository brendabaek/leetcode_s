## https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        print(root)
        if root == None : return True
        if root.left == None and root.right == None : return True
        elif root.left != None and root.right != None :
            left = root.left
            right = root.right    
            ans = self.compare_tree(left, right)
            return ans
        else : return False

    def compare_tree(self, left, right) :
        if left.val == right.val :
            if left.left == None and right.right == None :
                if left.right == None and right.left == None :
                    return True
                elif left.right != None and right.left != None :
                    if left.right.val == right.left.val :
                        return self.compare_tree(left.right, right.left)
                    else : return False
                else : return False

            elif left.left != None and right.right != None :
                if self.compare_tree(left.left, right.right) == False : return False
                else :
                    if left.right == None and right.left == None : return True
                    elif left.right != None and right.left != None :
                        return self.compare_tree(left.right, right.left)
                    else : return False
            else : return False
        else : return False
