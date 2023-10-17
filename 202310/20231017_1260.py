## https://leetcode.com/problems/shift-2d-grid/

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        r_shift, c_shift = (k // c) % r, k % c
        grid = grid[-r_shift:] + grid[:-r_shift]
        for i in range(r) :
            for _ in range(c_shift) :
                grid[i].insert(0, grid[i-1].pop())
        return grid