## https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        while nums != []:
            if len(nums) == len(set(nums)): return ans
            else: ans += 1; nums = nums[3:]
        return ans