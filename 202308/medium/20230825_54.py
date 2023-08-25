## https://leetcode.com/problems/spiral-matrix/

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] : return []

        ans = []
        while matrix != [] :
            ans += matrix.pop(0)

            for i in range(len(matrix)-1) :
                if matrix[i] == [] : return ans
                ans += [matrix[i].pop()]
                
            if matrix == [] : return ans
            ans += matrix.pop()[::-1]

            for j in range(len(matrix)-1, -1, -1) :
                if matrix[j] == [] : return ans
                ans += [matrix[j].pop(0)]
            
        return ans