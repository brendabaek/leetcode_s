## https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n1, n2 = 0, 1
        for i in str(n):
            n1 += int(i)
            n2 *= int(i)
        return True if n % (n1 + n2) == 0 else False