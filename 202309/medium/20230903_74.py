## https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix[0][0] == target : return True
        elif matrix[0][0] > target : return False
        elif matrix[-1][-1] < target : return False

        if len(matrix) == 1 : return target in matrix[0]
        for i in range(1, len(matrix)) :
            if matrix[i][0] == target : return True
            elif matrix[i][0] > target :
                return target in matrix[i-1]
        return target in matrix[i]