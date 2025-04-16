## https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        c, ans = 0, 0
        for dim in dimensions:
            d = ((dim[0] ** 2) + (dim[1] ** 2)) ** 0.5
            if d > c: ans = dim[0] * dim[1]; c = d
            elif d == c: ans = max(ans, dim[0] * dim[1])
        return ans