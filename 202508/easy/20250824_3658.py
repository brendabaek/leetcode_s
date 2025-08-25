## https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd, sumEven, ans = 0, 0, 1
        for i in range(1, n * 2 , 2): sumOdd, sumEven = sumOdd + i, sumEven + i + 1
        while sumOdd > 1:
            for i in range(2, sumOdd):
                if sumOdd % i == 0 and sumEven % i == 0:
                    sumOdd, sumEven, ans = sumOdd // i, sumEven // i, ans * i
                    break
                if i == sumOdd - 1: return ans
            if sumOdd == 2 and sumEven % 2 != 0: return ans
        return ans