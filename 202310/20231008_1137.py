## https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        f, s, t = 0, 1, 1
        if n == 0 : return f
        elif n == 1 : return s
        for i in range(n-2) : f, s, t = s, t, f+s+t
        return t