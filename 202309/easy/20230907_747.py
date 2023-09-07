## https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num, idx = max(nums), nums.index(max(nums))
        nums.pop(idx)
        if max(nums) * 2 <= num : return idx
        else : return -1