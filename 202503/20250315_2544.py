## https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans = 0
        while n > 0 :
            ans += n % 10; n //= 10
            if n == 0 : return ans
            ans -= n % 10; n //= 10
        return -ans