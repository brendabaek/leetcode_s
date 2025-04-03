## https://leetcode.com/problems/minimum-right-shifts-to-sort-the-array/

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        idx = nums.index(min(nums))
        nums = nums[idx:] + nums[:idx]
        p = nums[0]
        for num in nums[1:] :
            if num <= p : return -1
            else : p = num
        return 0 if idx == 0 else len(nums) - idx