## https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2 : return False
        nums.sort()
        cnt = 1
        for num in nums[:-1] :
            if cnt == num : cnt += 1
            else : return False
        return True if nums[-1] == nums[-2] else False