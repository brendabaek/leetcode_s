## https://leetcode.com/problems/degree-of-an-array/

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        opp, dics, ans = nums[::-1], {}, len(nums)
        for n in nums :
            try : dics[n] += 1
            except : dics[n] = 1
        m = max(dics.values())
        for d in dics :
            if dics[d] == m :
                ans = min(ans, (len(nums) - opp.index(d) - nums.index(d)))
        return ans
                