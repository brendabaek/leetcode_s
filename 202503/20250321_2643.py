## https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx, c = 0, 0
        for i in range(len(mat)) :
            if mat[i].count(1) > c : idx, c = i, mat[i].count(1)
        return [idx, c]