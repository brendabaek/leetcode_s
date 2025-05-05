## https://leetcode.com/problems/make-array-elements-equal-to-zero/

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s1, s2, ans = 0, sum(nums), 0
        for i in range(len(nums)):
            s1 += nums[i]
            s2 -= nums[i]
            if nums[i] == 0:
                if s1 == s2: ans += 2
                elif abs(s1 - s2) == 1: ans += 1
        return ans