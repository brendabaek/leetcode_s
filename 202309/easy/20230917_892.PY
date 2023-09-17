## https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ln, ans = len(grid), 0
        for i in range(ln) :
            for j in range(ln) :
                if j-1 < 0 : ans += grid[i][j]
                else : ans += abs(grid[i][j] - grid[i][j-1])
                if i-1 < 0 : ans += grid[i][j]
                else : ans += abs(grid[i][j] - grid[i-1][j])
                if grid[i][j] != 0 : ans += 2
            ans += grid[i][-1]
        ans += sum(grid[-1])
        return ans