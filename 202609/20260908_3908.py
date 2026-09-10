## https://leetcode.com/problems/valid-digit-number/

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        return True if str(x) in str(n) and str(x) != str(n)[0] else False