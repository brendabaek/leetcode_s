## https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if 9 * n < s: return -1
        ans = 0
        for i in range(n):
            ans = ans * 10 + min(9, s)
            s -= min(9, s)
        return ans