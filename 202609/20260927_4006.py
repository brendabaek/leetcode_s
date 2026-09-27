## https://leetcode.com/problems/count-valid-prefixes/

class Solution:
    def countValidPrefixes(self, s: str) -> int:
        cnt, ans = 0, 0
        for n in s:
            if n == "0": cnt += 1
            else: cnt -= 1
            if abs(cnt) <= 1: ans += 1
        return ans