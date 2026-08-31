## https://leetcode.com/problems/count-commas-in-range/

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000: return 0
        cnt = 3
        ans = n % 1000 + 1
        n = n // 1000
        while n > 0:
            t = n % 1000
            n = n // 1000
            ans += (t - 1) * (10 ** cnt)
            cnt += 3
        return ans