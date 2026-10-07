## https://leetcode.com/problems/cyclically-shift-rows-and-columns/

class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        # ans = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         c = (j - rowShift[i] + n) % n
        #         r = (i - (colShift[c]) + n) % n
        #         ans[r][c]= grid[i][j]
        # return ans
        
        n = len(rowShift)
        ans = [[] for _ in range(n)]
        for i in range(n): grid[i] = grid[i][rowShift[i]:] + grid[i][:rowShift[i]]
        grid += grid
        for j in range(n):
            for k in range(n):
                ans[k].append(grid[colShift[j]+k][j])
        return ans