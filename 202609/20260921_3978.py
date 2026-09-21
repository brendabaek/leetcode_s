## https://leetcode.com/problems/unique-middle-element/

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        return True if nums.count(nums[len(nums)//2]) == 1 else False