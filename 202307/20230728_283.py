## https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if nums == None : return
        cnt = 0
        for i in range(len(nums)) :
            if nums[cnt] == 0 :
                nums.append(nums.pop(cnt))
            else : cnt += 1
        return nums