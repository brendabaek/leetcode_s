## https://leetcode.com/problems/insert-interval/

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for i in intervals :
            if newInterval[0] > i[1] : ans.append(i)
            elif newInterval[1] < i[0] : ans.append(i)
            else : newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
        ans.append(newInterval)
        ans.sort()
        return ans