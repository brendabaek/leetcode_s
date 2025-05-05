## https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            c, p = n, 1
            while c > 0: p *= c % 10; c //= 10
            if p % t == 0: return n
            n += 1