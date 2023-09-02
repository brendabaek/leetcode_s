## https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        lst, r, c = [], len(matrix), len(matrix[0])
        for i in range(r) :
            for j in range(c) :
                if matrix[i][j] == 0 : lst.append([i, j])

        for l in lst :
            for i in range(r) : matrix[i][l[1]] = 0
            for j in range(c) : matrix[l[0]][j] = 0

        return