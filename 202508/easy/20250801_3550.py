## https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == sum(map(int, str(n))): return i
        return -1