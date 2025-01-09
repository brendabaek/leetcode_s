## https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        w, d = n // 7, n % 7
        for i in range(w) : ans += 28 + (7 * i)
        for j in range(d) : ans += w + j + 1
        return ans