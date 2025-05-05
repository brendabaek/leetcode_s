## https://leetcode.com/problems/stone-removal-game/

class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        for i in range(10, 0, -1):
            n -= i
            if n == 0: return ans == False
            elif n < 0: return ans
            ans = (ans == False)
        return ans