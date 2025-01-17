## https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans, check = -1, 10000
        for i in range(len(points)) :
            if points[i] == [x, y] : return i
            elif points[i][0] == x or points[i][1] == y :
                if check > abs(points[i][0] - x + points[i][1] - y) :
                    check = abs(points[i][0] - x + points[i][1] - y)
                    ans = i
        return ans