## https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        ln = len(matrix)
        n = set(i for i in range(1, ln+1))
        for i in range(ln) :
            if set(matrix[i]) != n : return False
            m = set()
            for j in range(ln) : m.add(matrix[j][i])
            if m != n : return False
        return True