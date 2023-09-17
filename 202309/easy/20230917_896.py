## https://leetcode.com/problems/monotonic-array/

class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3 : return True
        pre = 0
        for i in range(1, len(nums)) :
            crt = nums[i] - nums[i-1]
            if pre == 0 : pre = crt
            elif crt == 0 : pass
            elif crt != 0 and pre * crt < 0 : return False
            else : pre = crt
        return True