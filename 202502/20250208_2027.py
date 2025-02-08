## https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution:
    def minimumMoves(self, s: str) -> int:
        n, ans = 0, 0
        while n < len(s) :
            if s[n] == "X" : n, ans = n + 3, ans + 1
            else : n += 1
        return ans