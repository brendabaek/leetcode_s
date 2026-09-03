## https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        num, l, ans = 0, 1, 100
        for i in range(len(nums)):
            if nums[i] != 0: num = nums[i]; break
        if num == 0: return -1
        for j in range(i + 1, len(nums)):
            if nums[j] == 0: l += 1
            elif nums[j] != num:
                num, l, ans = nums[j], 1, min(ans, l)
            else: l = 1
        return ans if ans != 100 else -1