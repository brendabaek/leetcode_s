## https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = sum(i for i in range(1, n+1))
        for j in range(1, (n // m) + 1) : ans -= m * j * 2
        return ans