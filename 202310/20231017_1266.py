## https://leetcode.com/problems/minimum-time-visiting-all-points/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)) :
            x1, y1 = points[i]
            x0, y0 = points[i-1]
            x, y = abs(x1-x0), abs(y1-y0)
            ans += max(x, y)
        return ans