## https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n_idx, p_idx = 0, len(nums)-1
        while n_idx < p_idx and nums[n_idx] < 0 and nums[p_idx] > 0 :
            if nums[n_idx] > -nums[p_idx] : p_idx -= 1
            elif nums[n_idx] < -nums[p_idx] : n_idx += 1
            else : return nums[p_idx]
        return -1