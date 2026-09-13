## https://leetcode.com/problems/check-adjacent-digit-differences/

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = ord(s[0])
        for l in s[1:]:
            if abs(n  - ord(l)) > 2: return False
            else: n = ord(l)
        return True