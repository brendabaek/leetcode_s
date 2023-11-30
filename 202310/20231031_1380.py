## https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r, ans = len(matrix), []
        for mat in matrix :
            num = min(mat)
            ans.append(num)
            idx = mat.index(num)
            for i in range(r) :
                if matrix[i][idx] > num :
                    ans.pop()
                    break
        return ans