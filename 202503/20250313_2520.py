## https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        n, ans = num, 0
        while n > 0 :
            if num % (n % 10) == 0 : ans += 1
            n //= 10
        return ans