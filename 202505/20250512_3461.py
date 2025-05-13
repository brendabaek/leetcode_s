## https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s, t, n = list(s), int(s[0]), ""
            for i in range(1, len(s)):
                t += int(s[i])
                n += str(t % 10)
                t -= int(s[i-1])
            s = n
        return True if s[0] == s[1] else False