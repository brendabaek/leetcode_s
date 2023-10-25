## https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r, c, ans = len(mat), len(mat[0]), []
        dics = {i:[] for i in range(c+1)}
        for i in range(r) : dics[mat[i].count(1)] += [i]
        for j in range(c+1) : ans += dics[j]
        return ans[:k]