## https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        
        ans, left, right = [], intervals[0][0], intervals[0][1]
        for i in intervals :
            if i[0] <= right :
                right = max(right, i[1])
            else :
                ans.append([left, right])
                left, right = i[0], i[1]
        
        ans.append([left, right])
        return ans