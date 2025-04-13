## https://leetcode.com/problems/find-champion-i/

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        ans, c = 0, 0
        for idx, g in enumerate(grid) :
            if c < sum(g) : c = sum(g); ans = idx
        return ans