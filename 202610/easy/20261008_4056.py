## https://leetcode.com/problems/number-of-intersecting-interval-pairs-i/

class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        ln, ans = len(intervals), 0
        for i in range(ln):
            e = intervals[i][1]
            for j in range(i + 1, ln):
                if intervals[j][0] > e: break
                else: ans += 1
        return ans