## https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        idx, sums = 1, 0
        while idx < len(nums) :
            if nums[idx-1] + 1 == nums[idx] : idx += 1
            else : sums = sum(nums[:idx]); break
        if sums == 0 : sums = sum(nums)
        for i in range(sums, sums*1000):
            if i not in nums: return i