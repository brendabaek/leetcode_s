## https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, c, right, = 0, 0, sum(nums)
        for i in range(len(nums)) :
            left += c
            c = nums[i]
            right -= c
            if left == right : return i
        return -1
