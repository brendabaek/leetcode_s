## https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        r, c = [0] * m, [0] * n
        for i, j in indices :
            r[i] += 1
            c[j] += 1
        ans = 0
        for i in r :
            for j in c :
                if (i+j) % 2 == 1 : ans += 1
        return ans