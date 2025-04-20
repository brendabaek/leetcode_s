## https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        ln, rs = len(s), s[::-1]
        if ln < 2: return False
        for i in range(ln-1):
            w = s[i:i+2]
            if w in rs: return True
        return False