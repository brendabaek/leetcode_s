## https://leetcode.com/problems/find-the-highest-altitude/description/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, a = 0, 0
        for g in gain :
            a += g
            ans = max(ans, a)
        return ans