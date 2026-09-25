## https://leetcode.com/problems/even-number-of-knight-moves/

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return True if (sum(start) - sum(target)) % 2 == 0 else False