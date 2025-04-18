## https://leetcode.com/problems/modify-the-matrix/

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dics = {i:-1 for i in range(n)}
        for j in range(m):
            for k in range(n):
                if matrix[j][k] == -1:
                    if dics[k] == -1:
                        for l in range(m):
                            dics[k] = max(dics[k], matrix[l][k])
                    matrix[j][k] = dics[k]
        return matrix