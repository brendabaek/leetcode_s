## https://leetcode.com/problems/trionic-array-i/

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        p = 0
        for i in range(1, len(nums)):
            g = nums[i] - nums[i-1]
            if g == 0: return False
            elif p == 0 and g > 0: p = 1
            elif p == 1 and g < 0: p = 2
            elif p == 2 and g > 0: p = 3
            elif p == 3 and g < 0: return False
            elif p == 0: return False
        return True if p == 3 else False