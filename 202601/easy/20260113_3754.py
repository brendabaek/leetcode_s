## https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n, x, s = str(n), '0', 0
        for i in n:
            if i != '0': x += i
        for j in x[1:]: s += int(j)
        return int(x) * s