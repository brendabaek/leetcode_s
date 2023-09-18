## https://leetcode.com/problems/smallest-range-i/

class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max((max(nums) - k - min(nums) - k ), 0)