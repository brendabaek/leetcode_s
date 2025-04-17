## https://leetcode.com/problems/type-of-triangle/

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if sum(nums[:2]) <= nums[2]: return "none"
        if len(set(nums)) == 1: return "equilateral"
        elif len(set(nums)) == 2: return "isosceles"
        else: return "scalene" 