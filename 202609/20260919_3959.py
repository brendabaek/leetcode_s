## https://leetcode.com/problems/check-good-integer/

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum, squareSum = 0, 0
        while n > 0:
            d = n % 10
            digitSum += d
            squareSum += d ** 2
            n = n // 10
        return True if squareSum - digitSum >= 50 else False