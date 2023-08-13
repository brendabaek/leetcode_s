## https://leetcode.com/problems/teemo-attacking/

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if duration == 0 : return 0

        ans, s = 0, -1
        for i in timeSeries :
            if i > s : ans += duration
            else : ans += (i + duration - 1) - s
            s = i + duration - 1
        return ans