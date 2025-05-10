## https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        check, lst = True, []
        for g in grid:
            if check == True: lst += g; check = False
            else: lst += g[::-1]; check = True
        return [i for i in lst[::2]]