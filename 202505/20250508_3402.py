## https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for j in range(len(grid[0])):
            p = grid[0][j]
            for i in range(1, len(grid)):
                if grid[i][j] <= p: ans += (p + 1) - grid[i][j]; p = p + 1
                else: p = grid[i][j]
        return ans