## https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for g in grid :
            for n in g[::-1] :
                if n < 0 : ans += 1
                else : break
        return ans