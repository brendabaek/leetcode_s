## https://leetcode.com/problems/minimum-rotations-to-dial-a-number-i/

class Solution:
    def minRotations(self, s: str) -> int:
        p, ans = ord("0"), 0
        for l in s:
            n = ord(l)
            ans += min(abs(p - n), 10 - abs(p - n))
            p = n
        return ans