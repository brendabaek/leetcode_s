## https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        s, e = x, x + k - 1
        while s < e:
            grid[s][y:y + k], grid[e][y:y+k] = grid[e][y:y + k], grid[s][y:y+k]
            s += 1; e -= 1
        return grid