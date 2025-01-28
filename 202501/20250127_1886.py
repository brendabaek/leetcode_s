## https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if mat == target : return True
        ln = len(mat)
        for _ in range(3) :
            lst = [[] for _ in range(ln)]
            for i in range(ln-1, -1, -1) :
                for j in range(ln) :
                    lst[j].append(mat[i][j])
            if target == lst : return True
            else : mat = lst
        return False