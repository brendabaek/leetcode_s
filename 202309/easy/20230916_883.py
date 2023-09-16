## https://leetcode.com/problems/projection-area-of-3d-shapes/

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x, y, z, tmp, g = 0, 0, 0, 0, len(grid)
        for i in range(g) :
            x += max(grid[i])
            z += g - grid[i].count(0)
            for j in range(g) :
                tmp = max(tmp, grid[j][i])
            y += tmp
            tmp = 0
        return x + y + z