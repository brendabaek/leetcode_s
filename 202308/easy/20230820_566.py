## https://leetcode.com/problems/reshape-the-matrix/

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        lst, ans = [], []
        for i in range(len(mat)) :
            for j in range(len(mat[0])) : lst.append(mat[i][j])
        if len(lst) != (r*c) : return mat
        for i in range(r) :
            tmp = []
            for j in range(c) : tmp.append(lst.pop(0))
            ans.append(tmp)
        return ans