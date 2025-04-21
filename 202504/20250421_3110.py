## https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        ln, ans = len(s), 0
        for i in range(1, ln): ans += abs(ord(s[i-1]) - ord(s[i]))
        return ans