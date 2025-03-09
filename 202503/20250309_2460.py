## https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        idx, ln = 0, len(nums)
        while idx < ln - 1 :
            if nums[idx] == nums[idx+1] : nums[idx], nums[idx+1] = nums[idx] * 2, 0
            idx += 1
        idx, cnt = 0, ln - nums.count(0)
        while idx < ln :
            if nums[idx] == 0 and idx < cnt : nums.append(nums.pop(idx))
            else : idx += 1
        return nums