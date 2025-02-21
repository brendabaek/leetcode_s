## https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        n = (int(correct[:2]) * 60 + int(correct[-2:])) - (int(current[:2]) * 60 + int(current[-2:]))
        units, ans = [60, 15, 5], 0
        if n < 0 : n += 1440
        for unit in units : n, ans = n % unit, ans + (n // unit)
        return ans + n