## https://leetcode.com/problems/find-minimum-log-transportation-cost/

class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        ans = 0
        if n > k: ans += k * (n - k)
        if m > k: ans += k * (m - k)
        return ans