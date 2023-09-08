## https://leetcode.com/problems/toeplitz-matrix/

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r, c = len(matrix), len(matrix[0])
        for i in range(r-1) :
            row, col, check = i, 0, matrix[i][0]
            while row < r and col < c :
                if matrix[row][col] != check : return False
                row += 1; col += 1
        for j in range(1, c-1) :
            row, col, check = 0, j, matrix[0][j]
            while row < r and col < c :
                if matrix[row][col] != check : return False
                row += 1; col += 1
        return True