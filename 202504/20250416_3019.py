## https://leetcode.com/problems/number-of-changing-keys/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s, ln, ans, p = s.lower(), len(s), 0, s[0].lower()
        for i in range(1, ln):
            if p != s[i]: p = s[i]; ans += 1
        return ans