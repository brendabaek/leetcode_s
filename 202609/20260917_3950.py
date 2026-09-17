## https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        n = bin(n)
        return False if n.count("11") != 1 or "111" in n else True