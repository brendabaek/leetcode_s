## https://leetcode.com/problems/check-if-grid-satisfies-conditions/

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            if grid[0][i] == grid[0][i-1]: return False
        for j in range(1, m):
            if grid[j] != grid[j-1]: return False
        return True