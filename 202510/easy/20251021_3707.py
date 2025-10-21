## https://leetcode.com/problems/equal-score-substrings/

class Solution:
    def scoreBalance(self, s: str) -> bool:
        s1, s2, i1, i2 = 0, 0, 0, len(s) - 1
        while i1 <= i2:
            if s1 <= s2:
                s1 += ord(s[i1]) - 96
                i1 += 1
            else:
                s2 += ord(s[i2]) - 96
                i2 -= 1
        return s1 == s2