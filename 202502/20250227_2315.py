## https://leetcode.com/problems/count-asterisks/

class Solution:
    def countAsterisks(self, s: str) -> int:
        s, ans = s.split("|"), 0
        for i in range(0, len(s), 2) : ans += s[i].count("*")
        return ans