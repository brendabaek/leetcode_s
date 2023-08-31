## https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt, ans = 1, 1
        for i in range(1, len(nums)) :
            if nums[i-1] < nums[i] :
                cnt += 1
            else :
                ans = max(ans, cnt)
                cnt = 1
        
        return max(ans, cnt)