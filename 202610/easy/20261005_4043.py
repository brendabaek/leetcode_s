## https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/

class Solution:
    def countRotations(self, s: str, k: int) -> int:
        p, cnt, ln, ans = s[0], 0, len(s), 0
        for l in s[1:]:
            if l == p: cnt += 1
            else: p = l
        for _ in range(ln):
            if s[0] == s[1]: cnt -= 1
            if s[0] == s[-1]: cnt += 1
            if cnt == k: ans += 1
            s = s[1:] + s[0]
        return ans