## https://leetcode.com/problems/total-distance-traveled/

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5 and additionalTank > 0 : ans += 5; mainTank -= 4; additionalTank -= 1
        return (ans + mainTank) * 10