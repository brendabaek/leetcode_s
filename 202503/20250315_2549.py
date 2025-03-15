## https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution:
    def distinctIntegers(self, n: int) -> int:
        return max(1, n - 1)