## https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        c = nums.count(0)
        z = nums[:-c-1:-1].count(0)
        return c - z