## https://leetcode.com/problems/find-the-pivot-integer/

class Solution:
    def pivotInteger(self, n: int) -> int:
        m, s, e = 1, 0, 0
        while m <= n :
            if s == e and m == n : return m
            elif s == e : s, e = s + m, e + n; m, n = m + 1, n - 1
            elif s < e : s = s + m; m += 1
            else : e = e + n; n -= 1
        return -1