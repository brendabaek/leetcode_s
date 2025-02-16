## https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution:
    def countElements(self, nums: List[int]) -> int:
        return max(len(nums) - nums.count(max(nums)) - nums.count(min(nums)), 0)