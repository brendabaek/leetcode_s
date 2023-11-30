## https://leetcode.com/problems/special-positions-in-a-binary-matrix/

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r, c, ans = len(mat), len(mat[0]), 0
        for i in range(r) :
            if sum(mat[i]) != 1 : continue
            else :
                check = True
                idx = mat[i].index(1)
                for j in range(i-1, i-r, -1) :
                    if mat[j][idx] == 1 :
                        check = False; break
                if check == True : ans += 1
        return ans
