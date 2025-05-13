## https://leetcode.com/problems/transform-array-by-parity/

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)): nums[i] %= 2
        nums.sort()
        return nums

        # ln, o = len(nums), 0
        # for n in nums: o += (n % 2)
        # return [0] * (ln - o) + [1] * o