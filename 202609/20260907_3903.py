## https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        s, e = nums[0], min(nums)
        for i in range(len(nums)):
            if nums[i] > s: s = nums[i]
            if nums[i-1] == e: e = min(nums[i:])
            if s - e <= k: return i
        return -1