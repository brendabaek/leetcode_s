## https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        p = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] - p) % 2 == 0: return False
            else: p = nums[i]
        return True