## https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n) :
            num1, num2 = str(i), str(n-i)
            if ('0' not in num1) and ('0' not in num2) :
                return [i, n-i]