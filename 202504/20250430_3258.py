## https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ln, ans = len(s), 0
        for i in range(ln):
            z, o = 0, 0
            for j in range(i, ln):
                if s[j] == "0": z += 1
                else: o += 1
                if z <= k or o <= k: ans += 1
                elif z > k and o > k: break
        return ans