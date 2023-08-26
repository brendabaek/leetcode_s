## https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        crt = nums[0]
        for i in range(1, len(nums)) :
            if crt == 0 : return False
            crt = max(crt-1, nums[i])
        return True


        if len(nums) == 1 : return True
        return self.find_answer(nums, len(nums))

    def find_answer(self, nums, target) :
        max_number, max_idx = 0, 0
        for i in range(1, nums[0]+1) :
            if i + nums[i] >= len(nums)-1 : return True
            if i + nums[i] >= max_number and nums[i] != 0 :
                max_number = nums[i]
                max_idx = i

        if target - max_idx <= 0 : return True
        if max_number == 0 and max_idx == 0 : return False
        return self.find_answer(nums[max_idx:], target-max_idx)