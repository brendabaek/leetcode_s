## https://leetcode.com/problems/valid-boomerang/

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # points.sort()
        if points[0] == points[1] or points[1] == points[2] or points[2] == points[0] : return False
        if points[0][0] == points[1][0] and points[1][0] == points[2][0] : return False
        if points[0][1] == points[1][1] and points[1][1] == points[2][1] : return False
        try :
            if (int(points[0][0]-points[1][0]) / int(points[1][0]-points[2][0])) == \
                (int(points[0][1]-points[1][1]) / int(points[1][1]-points[2][1])) : return False
        except : return True
        return True