## https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.idx = {}
        self.values = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                self.idx[(i, j)] = grid[i][j]
                self.values[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int, ans = 0) -> int:
        m, n = self.values[value]
        for i, j in [(m - 1, n), (m + 1, n), (m, n - 1), (m, n + 1)]:
            if (i, j) in self.idx: ans += self.idx[(i, j)]
        return ans

    def diagonalSum(self, value: int, ans = 0) -> int:
        m, n = self.values[value]
        for i, j in [(m - 1, n - 1), (m - 1, n + 1), (m + 1, n - 1), (m + 1, n + 1)]:
            if (i, j) in self.idx: ans += self.idx[(i, j)]
        return ans

    # def __init__(self, grid: List[List[int]]):
    #     self.grid = grid
    #     self.ln = len(grid) - 1        

    # def adjacentSum(self, value: int) -> int:
    #     for i in range(self.ln + 1):
    #         if value in self.grid[i]:
    #             m, n = i, self.grid[i].index(value)
    #     ans = 0
    #     if m > 0: ans += self.grid[m-1][n]
    #     if m < self.ln: ans += self.grid[m+1][n]
    #     if n > 0: ans += self.grid[m][n-1]
    #     if n < self.ln: ans += self.grid[m][n+1]
    #     return ans

    # def diagonalSum(self, value: int) -> int:
    #     for i in range(self.ln + 1):
    #         if value in self.grid[i]:
    #             m, n = i, self.grid[i].index(value)
    #     ans = 0
    #     if m > 0 and n > 0: ans += self.grid[m-1][n-1]
    #     if m > 0 and n < self.ln: ans += self.grid[m-1][n+1]
    #     if m < self.ln and n > 0: ans += self.grid[m+1][n-1]
    #     if m < self.ln and n < self.ln: ans += self.grid[m+1][n+1]
    #     return ans

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)