## https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if len(nums) == 0 : return nums
        elif len(nums) == 1 :
            node = TreeNode(nums[0])
            return node
        elif len(nums) == 2 :
            node = TreeNode(min(nums))
            node.right = TreeNode(max(nums))
            return node
        else :
            nums = sorted(nums)
            ln = len(nums)
            nums1 = nums[:ln//2]
            nums2 = nums[ln//2+1:]
            node = TreeNode(nums[ln//2])

            node.left = self.make_node(nums1, node.left)
            node.right = self.make_node(nums2, node.right)
            return node

    def make_node(self, nums, node) :
        ln = len(nums)
        target = ln // 2
        node = TreeNode(nums[target])

        if ln == 1 :
            return node
        elif ln == 2 :
            node.left = TreeNode(nums[0])
            return node
        elif ln == 3 :
            node.left = TreeNode(min(nums))
            node.right = TreeNode(max(nums))
            return node
        else :
            node.left = self.make_node(nums[:ln//2], node.left)
            node.right = self.make_node(nums[ln//2+1:], node.right)
            return node