## https://leetcode.com/problems/count-monobit-integers/

class Solution:
    def countMonobit(self, n: int) -> int:
        n, ans = n + 1, 1
        while n > 1: ans += 1; n //= 2
        return ans