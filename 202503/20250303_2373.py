## https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # n = len(grid)
        # ans = [[0 for _ in range(n-2)] for _ in range(n-2)]
        # for i in range(n-2) :
        #     for j in range(n-2) :
        #         m = 0
        #         new_grid = [g[j:j+3] for g in grid[i:i+3]]
        #         for k in new_grid : m = max(m, max(k))
        #         ans[i][j] = m
        # return ans

        n = len(grid)
        ans = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(n-2) :
            for j in range(n-2) :
                ans[i][j] = max(grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2], grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
        return ans