## https://leetcode.com/problems/count-partitions-with-even-sum-difference/

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        l, r, ans = 0, sum(nums), 0
        for i in range(len(nums) - 1):
            l += nums[i]; r -= nums[i]
            if (l - r) % 2 == 0: ans += 1
        return ans