## https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        l = time % (2 * (n - 1))
        return l + 1 if l < (n - 1) else abs(l - ((2 * n) - 1))