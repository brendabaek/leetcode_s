## https://leetcode.com/problems/sum-of-compatible-numbers-in-range-i/

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        ans = 0
        for i in range(max(0, n-k), n+k+1):
            if n & i == 0: ans += i
        return ans