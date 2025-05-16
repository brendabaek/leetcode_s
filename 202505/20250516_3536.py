## https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution:
    def maxProduct(self, n: int) -> int:
        l = []
        while n > 0: l.append(n % 10); n //= 10
        l.sort(reverse = True)
        return l[0] * l[1]