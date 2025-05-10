## https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)): ans = max(ans, abs(nums[i] - nums[i - 1]))
        return ans