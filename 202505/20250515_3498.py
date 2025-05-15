## https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)) : ans += abs(ord(s[i]) - 123) * (i + 1)
        return ans