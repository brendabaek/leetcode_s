## https://leetcode.com/problems/find-the-peaks/

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ln, ans = len(mountain), []
        p, m = mountain[0], mountain[1]
        for i in range(2, ln):
            if p < m and m > mountain[i] : ans.append(i-1)
            p, m = m, mountain[i]
        return ans