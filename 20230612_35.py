## https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target in nums : return nums.index(target)
        
        cnt = 0

        for i in range(len(nums)) :
            if nums[i] < target :
                cnt += 1
            else : return cnt
        
        return cnt