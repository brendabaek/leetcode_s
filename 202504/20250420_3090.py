## https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        tmp, ans = s[0], 0
        for i in range(1, len(s)):
            if tmp.count(s[i]) >= 2:
                ans = max(ans, len(tmp))
                while tmp.count(s[i]) >= 2: tmp = tmp[1:]
            tmp += s[i]
        return max(ans, len(tmp))