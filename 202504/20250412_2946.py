## https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k, ans = k % n, []
        for i in range(m):
            if m % 2 == 0 : ans.append(mat[i][k:] + mat[i][:k])
            else : ans.append(mat[i][-k:] + mat[i][:-k])
        return True if mat == ans else False