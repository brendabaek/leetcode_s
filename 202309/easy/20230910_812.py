## https://leetcode.com/problems/largest-triangle-area/

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ans, ln = 0, len(points)
        for i in range(ln-2) :
            for j in range(i, ln-1) :
                for k in range(j, ln) :
                    ans = max(ans, float(abs((((points[i][0]*points[j][1])
                                                + (points[j][0]*points[k][1])
                                                + (points[k][0]*points[i][1]))
                                            - ((points[i][0]*points[k][1])
                                                + (points[j][0]*points[i][1])
                                                + (points[k][0]*points[j][1]))
                                            )))/2)
        return ans
