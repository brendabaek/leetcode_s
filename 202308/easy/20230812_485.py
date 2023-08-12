## https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sav, cnt = 0, 0
        for i in nums :
            if i == 1 : cnt += 1
            else :
                sav = max(sav, cnt)
                cnt = 0        
        return max(sav, cnt)