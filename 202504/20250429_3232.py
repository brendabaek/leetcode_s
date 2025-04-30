## https://leetcode.com/problems/find-if-digit-game-can-be-won/

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        nums.sort()
        s1, s2 = 0, 0
        for i in range(len(nums)):
            if nums[i] < 10: s1 += nums[i]
            else: s2 = sum(nums[i:]); break
        return False if s1 == s2 else True