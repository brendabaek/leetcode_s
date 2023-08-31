## https://leetcode.com/problems/minimum-path-sum/description/

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])

        sums = [[0 for j in range(c)] for i in range(r)]
        sums[0][0] = grid[0][0]
        
        for i in range(1, r) : sums[i][0] = sums[i-1][0] + grid[i][0]
        for j in range(1, c) : sums[0][j] = sums[0][j-1] + grid[0][j]
        
        for i in range(1, r) :
            for j in range(1, c) :
                sums[i][j] = min(sums[i-1][j], sums[i][j-1]) + grid[i][j]

        return sums[r-1][c-1]