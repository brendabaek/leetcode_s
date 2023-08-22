## https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ln = len(matrix)
        for i in range(ln-1, -1, -1) :
            for j in range(ln) :
                matrix[j].append(matrix[i].pop(0))
        return matrix
