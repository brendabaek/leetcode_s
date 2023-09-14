## https://leetcode.com/problems/transpose-matrix/description/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(matrix), len(matrix[0])
        for i in range(r) :
            for j in range(c) :
                try : matrix[j].append(matrix[i].pop(0))
                except : matrix.append([matrix[i].pop(0)])
        for i in range(r-c) : matrix.pop()
        else : return matrix