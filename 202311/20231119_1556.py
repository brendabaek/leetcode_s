## https://leetcode.com/problems/thousand-separator/

class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ln = len(s)
        if ln <= 3 : return s
        for i in range(ln//3, 0, -1) :
            s = s[:i*-3] + "." + s[i*-3:]
        return s.lstrip(".")