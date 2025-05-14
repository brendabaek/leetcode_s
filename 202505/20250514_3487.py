## https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if max(nums) <= 0: return max(nums)
        nums, ans = list(set(nums)), 0
        for n in nums:
            if n > 0: ans += n
        return ans