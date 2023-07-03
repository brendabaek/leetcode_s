## https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None : return None
        return self.postorder(root, [])

    def postorder(self, root, ans) :
        if root.left == None and root.right == None :
            ans.append(root.val)
        
        elif root.left != None and root.right == None :
            ans = self.postorder(root.left, ans)
            ans.append(root.val)

        elif root.left == None and root.right != None :
            ans = self.postorder(root.right, ans)
            ans.append(root.val)
            
        else : ## root.left != None and root.right != None
            ans = self.postorder(root.left, ans)
            ans = self.postorder(root.right, ans)
            ans.append(root.val)
        
        return ans