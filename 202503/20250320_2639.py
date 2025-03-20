## https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max([len(str(grid[i][j])) for i in range(len(grid))]) for j in range(len(grid[0]))]
        # m, n = len(grid), len(grid[0])
        # ans = [0] * n
        # for j in range(n) :
        #     l = 0
        #     for i in range(m) : l = max(l, len(str(grid[i][j])))
        #     ans[j] = l
        # return ans