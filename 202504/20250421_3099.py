## https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        d, n = 0, x
        while n > 0: d += n % 10; n //= 10
        return d if x % d == 0 else -1