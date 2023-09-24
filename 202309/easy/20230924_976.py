## https://leetcode.com/problems/largest-perimeter-triangle/

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ln = len(nums)
        for i in range(1, ln-1) :
            if nums[-i] >= (nums[-i-1] + nums[-i-2]) : pass
            else : return nums[-i] + nums[-i-1] + nums[-i-2]
        return 0