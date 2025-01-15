## https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

class Solution:
    def minOperations(self, s: str) -> int:
        ln, pre, ans = len(s), s[0], 0
        for i in s[1:] :
            if i == pre : ans += 1
            pre = "0" if pre == "1" else "1"
        return min(ln - ans, ans)