## https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return s if s.count(x) == 0 else s.replace(x, "") + x * s.count(x)
        # return s if s.count(y) == 0 else y * s.count(y) + s.replace(y, "")