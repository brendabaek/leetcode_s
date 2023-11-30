## https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r, c, ans = len(mat), len(mat[0]), 0
        for i in range(r) : ans += mat[i][i] + mat[i][-i-1]
        if r == c and r % 2 == 1 : ans -= mat[r//2][r//2]
        return ans