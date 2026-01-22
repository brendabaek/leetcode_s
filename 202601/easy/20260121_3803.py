## https://leetcode.com/problems/count-residue-prefixes/

class Solution:
    def residuePrefixes(self, s: str) -> int:
        d = set()
        ans = 0
        for i in range(len(s)):
            d.add(s[i])
            if len(d) >= 3: return ans
            if len(d) == (i + 1) % 3: ans += 1
        return ans