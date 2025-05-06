## https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution:
    def smallestNumber(self, n: int) -> int:
        return (2 ** (len(bin(n)) - 2)) - 1