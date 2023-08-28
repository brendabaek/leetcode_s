## https://leetcode.com/problems/maximum-average-subarray-i/

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        m, s = sum(nums[:k]), sum(nums[:k])
        for i in range(1, len(nums)-k+1) :
            s = s - nums[i-1] + nums[i+k-1]
            m = max(m, s)
            
        return float(m)/k