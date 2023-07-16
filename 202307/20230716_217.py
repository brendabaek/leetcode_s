## https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None : return
        nums.sort()
        while len(nums) > 1 :
            if nums[0] == nums[1] : return True
            else : nums.pop(0)
        # for i in range(len(nums)-1) :
        #     if nums[i] == nums[i+1] : return True
        return False