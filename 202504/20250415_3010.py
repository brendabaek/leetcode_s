## https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums.pop(0) + min(nums)
        nums.remove(min(nums))
        return ans + min(nums)