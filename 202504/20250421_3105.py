## https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ln, c, ans = len(nums), 1, 0
        for i in range(1, ln):
            if nums[i-1] < nums[i]: c += 1
            else: ans = max(ans, c); c = 1
        ans = max(ans, c); c = 1
        for i in range(1, ln):
            if nums[i-1] > nums[i]: c += 1
            else: ans = max(ans, c); c = 1
        return max(ans, c)