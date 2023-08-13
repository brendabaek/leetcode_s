## https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        pos = (dividend > 0) == (divisor > 0)
        d1, d2 = abs(dividend), abs(divisor)
        ans = 0
        while d1 >= d2 :
            tmp, cnt = d2, 1
            while d1 >= tmp :
                d1 = d1 - tmp
                ans += cnt
                tmp <<= 1
                cnt <<= 1

        if pos == True : return min(2147483647, ans)
        else : return max(-2147483648, -ans)