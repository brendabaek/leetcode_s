## https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        print("p : ", p)
        print("q : ", q)
        if p == q : return True
        elif p == None or q == None : return False
        else :
            if p.val == q.val :
                if p.left == None and q.left == None :
                    if p.right == None and q.right == None : return True
                    elif p.right != None and q.right != None :
                        if p.right.val == q.right.val :
                            ans = self.isSameTree(p.right, q.right)
                            if ans == False : return ans
                        else : return False
                    else : return False
                elif p.left != None and q.left != None :
                    if p.left.val == q.left.val :
                        ans = self.isSameTree(p.left, q.left)
                        if ans == False : return ans
                    else : return False
                else : return False

                if p.right == None and q.right == None : return True
                elif p.right != None and q.right != None :
                    ans = self.isSameTree(p.right, q.right)
                    if ans == False : return ans
                else : return False
                    
            else : return False
        return ans