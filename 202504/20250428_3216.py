## https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution:
    def getSmallestString(self, s: str) -> str:
        p = s[0]
        for i in range(1, len(s)):
            if p != "0" and (int(p) + int(s[i])) % 2 == 0 and p > s[i]: return s[:i-1] + s[i] + s[i-1] + s[i+1:]
            p = s[i]
        return s